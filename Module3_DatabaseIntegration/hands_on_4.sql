-- TASK 1 : Baseline Performance — No Indexes

-- 48. Run EXPLAIN (PostgreSQL) on the following query and save the output as a comment:  

EXPLAIN 
SELECT s.first_name, s.last_name, c.course_name 
FROM enrollments e   
JOIN students s ON s.student_id = e.student_id   
JOIN courses c ON c.course_id = e.course_id   
WHERE s.enrollment_year = 2022;

-- 49. Identify whether the query plan shows a Sequential Scan (Postgres) or Full Table Scan (MySQL) on any table.
-- Refer Task 1 Output

-- 50. Note the estimated cost in your comments.
-- Refer Task 1 Output

/* TASK 1 OUTPUT
college_db=# \i hands_on_4.sql
                                      QUERY PLAN                                                      
--------------------------------------------------------------------------------------
 Nested Loop  (cost=12.16..45.66 rows=11 width=554)
   ->  Hash Join  (cost=12.01..43.56 rows=11 width=240)
         Hash Cond: (e.student_id = s.student_id)
         ->  Seq Scan on enrollments e  (cost=0.00..27.00 rows=1700 width=8)
         ->  Hash  (cost=12.00..12.00 rows=1 width=240)
               ->  Seq Scan on students s  (cost=0.00..12.00 rows=1 width=240)
                     Filter: (enrollment_year = 2022)
   ->  Index Scan using courses_pkey on courses c  (cost=0.14..0.19 rows=1 width=322)
         Index Cond: (course_id = e.course_id)
(9 rows)
*/

-- TASK 2 : Add Indexes and Compare Plans

-- 51. Create a B-Tree index on students.enrollment_year.
CREATE INDEX idx_students_enrollment_year ON students(enrollment_year);

-- 52. Create a composite UNIQUE index on enrollments(student_id, course_id) — this also prevents duplicate enrollments.
CREATE UNIQUE INDEX idx_unique_student_course ON enrollments(student_id, course_id);

-- 53. Create an index on courses.course_code.
CREATE INDEX idx_courses_course_code ON courses(course_code);

-- 54. Re-run the EXPLAIN from Task 1 and compare the new plan to the baseline.
EXPLAIN 
SELECT s.first_name, s.last_name, c.course_name 
FROM enrollments e   
JOIN students s ON s.student_id = e.student_id   
JOIN courses c ON c.course_id = e.course_id   
WHERE s.enrollment_year = 2022;

-- 55. Create a partial index on enrollments(student_id) WHERE grade IS NULL to optimise lookups for unevaluated enrollments.
CREATE INDEX idx_partial_unevaluated_enrollments 
ON enrollments(student_id) 
WHERE grade IS NULL;

/* TASK 2 OUTPUT
college_db=# \i hands_on_4.sql
CREATE INDEX
CREATE INDEX
CREATE INDEX
                                  QUERY PLAN                                                          
------------------------------------------------------------------------------
 Nested Loop  (cost=1.14..3.39 rows=1 width=554)
   Join Filter: (c.course_id = e.course_id)
   ->  Hash Join  (cost=1.14..2.27 rows=1 width=240)
         Hash Cond: (e.student_id = s.student_id)
         ->  Seq Scan on enrollments e  (cost=0.00..1.10 rows=10 width=8)
         ->  Hash  (cost=1.12..1.12 rows=1 width=240)
               ->  Seq Scan on students s  (cost=0.00..1.12 rows=1 width=240)
                     Filter: (enrollment_year = 2022)
   ->  Seq Scan on courses c  (cost=0.00..1.05 rows=5 width=322)
(9 rows)

CREATE INDEX
*/

-- TASK 3 : Identify and Fix the N+1 Problem

-- 56. Simulate the N+1 problem in Python: fetch all enrollments with SELECT * FROM enrollments, then loop through each row and issue a separate SELECT to fetch the student's name. Count the total queries executed.
-- 57. Rewrite the script using a single JOIN query that retrieves all enrollment records with student names in one query.
-- 58. Compare the number of database round-trips between the two approaches and log the difference using Python's time module.
-- 59. Document in comments: in a real application with 10,000 enrollments, how many extra queries would the N+1 version issue?

/* TASK 3 OUTPUT

> python np1_test.py
N+1 Approach
Total Queries Executed: 11
Execution Latency Time: 0.0100 seconds

Optimized Approach
Total Queries Executed: 1
Execution Latency Time: 0.0068 seconds

The N+1 version would execute exactly 10,001 database queries (1 initial query to get 
the enrollment records, and 10,000 subsequent individual lookup queries for each row). 
This represents 10,000 extra, unnecessary database round trips, resulting in severe 
network overhead bottlenecks. The optimized JOIN version will always execute exactly 
1 single query, regardless of the row volume.
*/
