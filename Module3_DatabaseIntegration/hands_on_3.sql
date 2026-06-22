-- TASK 1 : Subqueries

-- 35. Find all students who are enrolled in more courses than the average number of enrollments per student.
WITH student_counts AS (
    SELECT student_id, COUNT(*) AS course_count
    FROM enrollments
    GROUP BY student_id
),
overall_avg AS (
    SELECT AVG(course_count) AS avg_courses 
    FROM student_counts
)
SELECT S.student_id, (S.first_name || ' ' || S.last_name) AS student_name, COUNT(E.course_id) AS total_enrolled
FROM students S
INNER JOIN enrollments E ON 
    S.student_id = E.student_id
GROUP BY S.student_id, S.first_name, S.last_name
HAVING COUNT(E.course_id) > (SELECT avg_courses FROM overall_avg);

-- 36. List courses in which all enrolled students have received a grade of 'A'.
SELECT C.course_id, C.course_code, C.course_name
FROM courses C
WHERE EXISTS (SELECT 1 FROM enrollments E WHERE E.course_id = C.course_id) -- Ensures at least someone is enrolled
  AND NOT EXISTS (
    SELECT 1 
    FROM enrollments E 
    WHERE E.course_id = C.course_id 
    AND (E.grade != 'A' OR E.grade IS NULL)
);

-- 37. Find the professor with the highest salary in each department using a correlated subquery.
SELECT p1.prof_name, p1.dept_id, p1.salary
FROM professors p1
WHERE p1.salary = (
    SELECT MAX(p2.salary)
    FROM professors p2
    WHERE p2.dept_id = p1.dept_id
);

-- 38. Using a subquery in the FROM clause, find departments where average salary exceeds 85,000.
SELECT dept.dept_name, summary.avg_salary
FROM (
    SELECT P.dept_id, AVG(P.salary) AS avg_salary
    FROM professors p
    GROUP BY P.dept_id
) AS summary 
INNER JOIN departments dept ON 
    summary.dept_id = dept.dept_id
WHERE summary.avg_salary > 85000;

/* TASK 1 OUTPUT
college_db=# \i hands_on_3.sql
 student_id | student_name | total_enrolled                                                                                        
------------+--------------+----------------
          5 | Vikram Das   |              2
          2 | Priya Suresh |              2
          1 | Arjun Mehta  |              2
          8 | Deepika Rao  |              2
(4 rows)


 course_id | course_code | course_name                                                                                             
-----------+-------------+-------------
(0 rows)


     prof_name      | dept_id |  salary                                                                                            
--------------------+---------+----------
 Dr. Anand Krishnan |       1 | 95000.00
 Dr. Sunil Rajan    |       2 | 82000.00
 Dr. Latha Gopal    |       3 | 79000.00
 Dr. Kartik Bose    |       4 | 76000.00
(4 rows)


    dept_name     |     avg_salary                                                                                                 
------------------+--------------------
 Computer Science | 91500.000000000000
(1 row)
*/

-- TASK 2 : Creating and Using Views

-- 39. Create a view vw_student_enrollment_summary showing each student's full name, department, number of courses enrolled in, and GPA (average grade converted: A=4, B=3, C=2, D=1, F=0).
CREATE VIEW vw_student_enrollment_summary AS
SELECT 
    (S.first_name || ' '  || S.last_name) AS full_name, D.dept_name, 
    COUNT(E.student_id) AS courses_enrolled, 
    AVG(
        CASE E.grade::text
            WHEN 'A' THEN 4
            WHEN 'B' THEN 3
            WHEN 'C' THEN 2
            WHEN 'D' THEN 1
            WHEN 'F' THEN 0
            ELSE NULL
        END
    ) AS gpa
FROM students S 
LEFT JOIN departments D ON
    S.dept_id = D.dept_id
LEFT JOIN enrollments E ON 
    S.student_id = E.student_id
GROUP BY S.student_id, S.first_name, S.last_name, D.dept_name;

-- 40. Create a view vw_course_stats showing course_name, course_code, total_enrollments, and avg_gpa for each course.
CREATE VIEW vw_course_stats AS
SELECT 
    C.course_name, C.course_code, COUNT(E.course_id) AS total_enrollments, 
    AVG(
        CASE E.grade::text
            WHEN 'A' THEN 4
            WHEN 'B' THEN 3
            WHEN 'C' THEN 2
            WHEN 'D' THEN 1
            WHEN 'F' THEN 0
            ELSE NULL
        END
    ) AS avg_gpa
FROM courses C
LEFT JOIN enrollments E ON
    C.course_id = E.course_id
GROUP BY C.course_id, C.course_name, C.course_code;

-- 41. Query vw_student_enrollment_summary to find students with GPA above 3.0.
SELECT * 
FROM vw_student_enrollment_summary
WHERE gpa > 3;

-- 42. Attempt to UPDATE a row through vw_student_enrollment_summary and document what happens. Research and document in your comments why multi-table views are generally not updatable.
UPDATE vw_student_enrollment_summary 
SET gpa = 4.0 
WHERE full_name = 'Aditya Kalidas';

-- 43. DROP both views and recreate vw_student_enrollment_summary as a view WITH CHECK OPTION (use a single-table subset view for this step).
DROP VIEW vw_student_enrollment_summary;
DROP VIEW vw_course_stats;

CREATE VIEW vw_student_enrollment_summary AS
SELECT 
    student_id, first_name, last_name, email, dept_id, enrollment_year
FROM students
WHERE dept_id = 3
WITH CHECK OPTION;

/* TASK 2 OUTPUT
college_db=# \i hands_on_3.sql
CREATE VIEW
CREATE VIEW
  full_name   |    dept_name     | courses_enrolled |        gpa         
--------------+------------------+------------------+--------------------
 Vikram Das   | Computer Science |                2 | 3.5000000000000000
 Deepika Rao  | Computer Science |                2 | 3.5000000000000000
 Rohan Verma  | Electronics      |                1 | 4.0000000000000000
 Arjun Mehta  | Computer Science |                2 | 3.5000000000000000
 Priya Suresh | Computer Science |                2 | 3.5000000000000000
(5 rows)


psql:hands_on_3.sql:133: ERROR:  cannot update view "vw_student_enrollment_summary"
DETAIL:  Views containing GROUP BY are not automatically updatable.
HINT:  To enable updating the view, provide an INSTEAD OF UPDATE trigger or an unconditional ON UPDATE DO INSTEAD rule.
DROP VIEW
DROP VIEW
CREATE VIEW
*/

-- TASK 3 : Stored Procedures and Transactions

-- 44. Write a function fn_enroll_student that accepts student_id, course_id, and enrollment_date, checks for duplicate enrollment, and inserts the record.
CREATE OR REPLACE FUNCTION fn_enroll_student(
    p_student_id INT, 
    p_course_id INT, 
    p_enrollment_date DATE
)
RETURNS TEXT AS $$
DECLARE
    already_enrolled INT;
BEGIN
    SELECT 1 INTO already_enrolled 
    FROM enrollments 
    WHERE student_id = p_student_id AND course_id = p_course_id;

    IF FOUND THEN
        RETURN 'Error: Student is already enrolled in this course.';
    ELSE
        INSERT INTO enrollments (student_id, course_id, enrollment_date)
        VALUES (p_student_id, p_course_id, p_enrollment_date);
        
        RETURN 'Success: Student enrolled successfully.';
    END IF;
END;
$$ LANGUAGE plpgsql;

SELECT fn_enroll_student(1, 5, '2025-04-10');
SELECT fn_enroll_student(1, 5, '2025-04-10');

-- 45. Write a procedure sp_transfer_student that moves a student from one department to another.
CREATE TABLE IF NOT EXISTS department_transfer_log (
    log_id SERIAL PRIMARY KEY,
    student_id INT,
    old_dept_id INT,
    new_dept_id INT,
    transfer_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE OR REPLACE PROCEDURE sp_transfer_student(
    p_student_id INT,
    p_new_dept_id INT
) AS $$
DECLARE
    v_old_dept_id INT;
BEGIN
    SELECT dept_id INTO v_old_dept_id FROM students WHERE student_id = p_student_id;

    UPDATE students 
    SET dept_id = p_new_dept_id 
    WHERE student_id = p_student_id;

    INSERT INTO department_transfer_log (student_id, old_dept_id, new_dept_id)
    VALUES (p_student_id, v_old_dept_id, p_new_dept_id);
END;
$$ LANGUAGE plpgsql;


-- 46. Test the transaction by manually introducing an error (e.g., invalid foreign key) and verify that the first UPDATE is also rolled back.
CALL sp_transfer_student(1, 9999); 


-- 47. Use SAVEPOINT to create a mid-transaction checkpoint: insert two enrollment records; set a SAVEPOINT after the first; deliberately fail the second; ROLLBACK TO SAVEPOINT and verify only the first record was saved.

BEGIN;

INSERT INTO enrollments (student_id, course_id, enrollment_date)
VALUES (2, 5, '2026-04-10');

SAVEPOINT first_insert_saved;

INSERT INTO enrollments (student_id, course_id, enrollment_date)
VALUES (2, 9999, '2026-04-10');

ROLLBACK TO SAVEPOINT first_insert_saved;

COMMIT;

SELECT * FROM enrollments WHERE student_id = 2 AND course_id = 5;

/* TASK 3 OUTPUT
college_db=# \i hands_on_3.sql
CREATE FUNCTION
            fn_enroll_student                                          
-----------------------------------------
 Success: Student enrolled successfully.
(1 row)


                 fn_enroll_student                                     
----------------------------------------------------
 Error: Student is already enrolled in this course.
(1 row)

CREATE TABLE
CREATE PROCEDURE
psql:hands_on_3.sql:228: ERROR:  insert or update on table "students" violates foreign key constraint "students_dept_id_fkey"
DETAIL:  Key (dept_id)=(9999) is not present in table "departments".
CONTEXT:  SQL statement "UPDATE students 
    SET dept_id = p_new_dept_id 
    WHERE student_id = p_student_id"
PL/pgSQL function sp_transfer_student(integer,integer) line 7 at SQL statement
BEGIN
INSERT 0 1
SAVEPOINT
psql:hands_on_3.sql:241: ERROR:  insert or update on table "enrollments" violates foreign key constraint "enrollments_course_id_fkey"
DETAIL:  Key (course_id)=(9999) is not present in table "courses".
ROLLBACK
COMMIT
 enrollment_id | student_id | course_id | enrollment_date | grade      
---------------+------------+-----------+-----------------+-------
            20 |          2 |         5 | 2026-04-10      | 
(1 row)
*/
