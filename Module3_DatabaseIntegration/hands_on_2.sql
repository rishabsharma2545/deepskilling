-- TASK 1 : Insert, Update and Delete Data

-- 15. Insert the sample data from the Common Schema section into all five tables.
-- executed in `sample_data.sql`

-- 16. Insert two additional students of your own choosing into the students table.
SELECT COUNT(*) AS Before_Insertion FROM students;

INSERT INTO students (first_name, last_name, email, date_of_birth, dept_id, enrollment_year) VALUES
  ('Akshit',  'Verma',    'akshit.verma@college.edu',    '2005-12-15', 3, 2023),
  ('Aditya',  'Kalidas',   'aditya.kalidas@college.edu',   '2003-01-01', 4, 2021);

SELECT COUNT(*) AS After_Insertion FROM students;

-- 17. Update the grade of student_id = 5 for course_id = 1 from 'C' to 'B'.
SELECT student_id, course_id, grade AS before_grade 
FROM enrollments WHERE student_id = 5 AND course_id = 1;

UPDATE enrollments
SET grade = 'B'
WHERE student_id = 5 AND course_id = 1;

SELECT student_id, course_id, grade AS after_grade 
FROM enrollments WHERE student_id = 5 AND course_id = 1;

-- 18. Delete enrollments where grade IS NULL (students who never received a grade).
SELECT COUNT(*) AS Before_Deletion FROM enrollments;

DELETE FROM enrollments
WHERE grade IS NULL;

SELECT COUNT(*) AS After_Deletion FROM enrollments;

-- 19. Verify row counts using SELECT COUNT(*) after each operation.
-- VIEW THE OUTPUT

/* TASK 1 OUTPUT
college_db-# \i hands_on_2.sql
 before_insertion                                                                                                  
------------------
                8
(1 row)


INSERT 0 2
 after_insertion                                                                                                   
-----------------
              10
(1 row)


 student_id | course_id | before_grade                                                                             
------------+-----------+--------------
          5 |         1 | C
(1 row)


UPDATE 1
 student_id | course_id | after_grade                                                                              
------------+-----------+-------------
          5 |         1 | B
(1 row)


 before_deletion                                                                                                   
-----------------
              12
(1 row)


DELETE 2
 after_deletion                                                                                                    
----------------
             10
(1 row)
*/

-- TASK 2 : Single-Table Queries and Filtering

-- 20. Retrieve all students enrolled in 2022, ordered by last_name alphabetically.
SELECT * 
FROM students
WHERE enrollment_year = 2022
ORDER BY last_name;

-- 21. Find all courses with more than 3 credits, sorted by credits descending.
SELECT *
FROM courses
WHERE credits > 3
ORDER BY credits DESC;

-- 22. List all professors whose salary is between 80,000 and 95,000.
SELECT *
FROM professors
WHERE salary BETWEEN 80000 AND 95000
ORDER BY salary DESC;

-- 23. Find all students whose email ends with '@college.edu' using the LIKE operator.
SELECT * 
FROM students
WHERE email LIKE '%@college.edu';

-- 24. Count the total number of students per enrollment_year.
SELECT enrollment_year, COUNT(student_id) AS total_students
FROM students
GROUP BY enrollment_year;

/* TASK 2 OUTPUT
college_db-# \i hands_on_2.sql
 student_id | first_name | last_name |          email           | date_of_birth | dept_id | enrollment_year 
------------+------------+-----------+--------------------------+---------------+---------+-----------------
          5 | Vikram     | Das       | vikram.das@college.edu   | 2003-09-14    |       1 |            2022
          1 | Arjun      | Mehta     | arjun.mehta@college.edu  | 2003-04-12    |       1 |            2022
          8 | Deepika    | Rao       | deepika.rao@college.edu  | 2003-08-09    |       1 |            2022
          2 | Priya      | Suresh    | priya.suresh@college.edu | 2003-07-25    |       1 |            2022
(4 rows)


 course_id |         course_name          | course_code | credits | dept_id | max_seats 
-----------+------------------------------+-------------+---------+---------+-----------
         1 | Data Structures & Algorithms | CS101       |       4 |       1 |        60
         3 | Object Oriented Programming  | CS103       |       4 |       1 |        60
(2 rows)


 professor_id |     prof_name      |        email        | dept_id |  salary       
--------------+--------------------+---------------------+---------+----------
            1 | Dr. Anand Krishnan | anand.k@college.edu |       1 | 95000.00
            2 | Dr. Meena Pillai   | meena.p@college.edu |       1 | 88000.00
            3 | Dr. Sunil Rajan    | sunil.r@college.edu |       2 | 82000.00
(3 rows)


 student_id | first_name | last_name |           email            | date_of_birth | dept_id | enrollment_year 
------------+------------+-----------+----------------------------+---------------+---------+-----------------
          1 | Arjun      | Mehta     | arjun.mehta@college.edu    | 2003-04-12    |       1 |            2022
          2 | Priya      | Suresh    | priya.suresh@college.edu   | 2003-07-25    |       1 |            2022
          3 | Rohan      | Verma     | rohan.verma@college.edu    | 2002-11-08    |       2 |            2021
          4 | Sneha      | Patel     | sneha.patel@college.edu    | 2004-01-30    |       3 |            2023
          5 | Vikram     | Das       | vikram.das@college.edu     | 2003-09-14    |       1 |            2022
          6 | Kavya      | Menon     | kavya.menon@college.edu    | 2002-05-17    |       2 |            2021
          7 | Aditya     | Singh     | aditya.singh@college.edu   | 2004-03-22    |       4 |            2023
          8 | Deepika    | Rao       | deepika.rao@college.edu    | 2003-08-09    |       1 |            2022
         12 | Akshit     | Verma     | akshit.verma@college.edu   | 2005-12-15    |       3 |            2023
         13 | Aditya     | Kalidas   | aditya.kalidas@college.edu | 2003-01-01    |       4 |            2021
(10 rows)


 enrollment_year | total_students                                                  
-----------------+----------------
            2022 |              4
            2023 |              3
            2021 |              3
(3 rows)
*/

-- TASK 3 : Multi-Table Joins

-- 25. List each student's full name (first_name + ' ' + last_name) alongside the name of their department. 
SELECT (first_name || ' ' || last_name) AS student_name, dept_name
FROM students s
LEFT JOIN 
    departments d ON s.dept_id = d.dept_id;

-- 26. Show each enrollment along with the student's name and the course name.
SELECT E.*, (S.first_name || ' ' || S.last_name) AS student_name, C.course_name
FROM enrollments E
INNER JOIN students S ON
    E.student_id = S.student_id
INNER JOIN courses C ON
    E.course_id = C.course_id;

-- 27. Find all students who are NOT enrolled in any course using a LEFT JOIN and WHERE ... IS NULL
SELECT * 
FROM students S
LEFT JOIN enrollments E ON
    S.student_id = E.student_id
WHERE enrollment_id IS NULL;

-- 28. Display every course along with the number of students enrolled in it. Courses with zero enrolments must still appear. 
SELECT C.course_id, C.course_name, COUNT(E.student_id) AS total_students
FROM courses C
LEFT JOIN enrollments E ON
    C.course_id = E.course_id
GROUP BY C.course_id, C.course_name
ORDER BY total_students;

-- 29. List each department along with its professors and their salaries. Include departments that have no professors yet.
SELECT D.*, professor_id, prof_name, salary
FROM departments D
LEFT JOIN professors P ON 
    D.dept_id = P.dept_id
ORDER BY D.dept_id;

/* TASK 3 OUTPUT
college_db-# \i hands_on_2.sql
  student_name  |    dept_name                                                                         
----------------+------------------
 Arjun Mehta    | Computer Science
 Priya Suresh   | Computer Science
 Rohan Verma    | Electronics
 Sneha Patel    | Mechanical
 Vikram Das     | Computer Science
 Kavya Menon    | Electronics
 Aditya Singh   | Civil
 Deepika Rao    | Computer Science
 Akshit Verma   | Mechanical
 Aditya Kalidas | Civil
(10 rows)


 enrollment_id | student_id | course_id | enrollment_date | grade | student_name |         course_name          
---------------+------------+-----------+-----------------+-------+--------------+------------------------------
             1 |          1 |         1 | 2022-07-01      | A     | Arjun Mehta  | Data Structures & Algorithms
             2 |          1 |         2 | 2022-07-01      | B     | Arjun Mehta  | Database Management Systems
             3 |          2 |         1 | 2022-07-01      | B     | Priya Suresh | Data Structures & Algorithms
             4 |          2 |         3 | 2022-07-01      | A     | Priya Suresh | Object Oriented Programming
             5 |          3 |         4 | 2021-07-01      | A     | Rohan Verma  | Circuit Theory
             8 |          5 |         2 | 2022-07-01      | A     | Vikram Das   | Database Management Systems
             9 |          6 |         4 | 2021-07-01      | B     | Kavya Menon  | Circuit Theory
            11 |          8 |         1 | 2022-07-01      | A     | Deepika Rao  | Data Structures & Algorithms
            12 |          8 |         3 | 2022-07-01      | B     | Deepika Rao  | Object Oriented Programming
             7 |          5 |         1 | 2022-07-01      | B     | Vikram Das   | Data Structures & Algorithms
(10 rows)


 student_id | first_name | last_name |           email            | date_of_birth | dept_id | enrollment_year | enrollment_id | student_id | course_id | enrollment_date | grade 
------------+------------+-----------+----------------------------+---------------+---------+-----------------+---------------+------------+-----------+-----------------+-------
         12 | Akshit     | Verma     | akshit.verma@college.edu   | 2005-12-15    |       3 |            2023 |               |            |           |                 | 
         13 | Aditya     | Kalidas   | aditya.kalidas@college.edu | 2003-01-01    |       4 |            2021 |               |            |           |                 | 
          4 | Sneha      | Patel     | sneha.patel@college.edu    | 2004-01-30    |       3 |            2023 |               |            |           |                 | 
          7 | Aditya     | Singh     | aditya.singh@college.edu   | 2004-03-22    |       4 |            2023 |               |            |           |                 | 
(4 rows)


 course_id |         course_name          | total_students                                             
-----------+------------------------------+----------------
         5 | Thermodynamics               |              0
         3 | Object Oriented Programming  |              2
         4 | Circuit Theory               |              2
         2 | Database Management Systems  |              2
         1 | Data Structures & Algorithms |              4
(5 rows)


 dept_id |    dept_name     |   head_of_dept    |  budget   | professor_id |     prof_name      |  salary  
---------+------------------+-------------------+-----------+--------------+--------------------+----------
       1 | Computer Science | Dr. Ramesh Kumar  | 850000.00 |            1 | Dr. Anand Krishnan | 95000.00
       1 | Computer Science | Dr. Ramesh Kumar  | 850000.00 |            2 | Dr. Meena Pillai   | 88000.00
       2 | Electronics      | Dr. Priya Nair    | 620000.00 |            3 | Dr. Sunil Rajan    | 82000.00
       3 | Mechanical       | Dr. Suresh Iyer   | 540000.00 |            4 | Dr. Latha Gopal    | 79000.00
       4 | Civil            | Dr. Ananya Sharma | 430000.00 |            5 | Dr. Kartik Bose    | 76000.00
(5 rows)
*/

-- TASK 4 : Aggregations and Grouping

-- 30. Calculate the total number of enrollments per course. Display course_name and enrollment_count.
SELECT C.course_name, COUNT(E.course_id) AS enrollment_count
FROM courses C
LEFT JOIN enrollments E ON
    C.course_id = E.course_id
GROUP BY C.course_id, C.course_name
ORDER BY enrollment_count DESC;

-- 31. Find the average salary of professors per department. Round to 2 decimal places.
SELECT D.dept_name, ROUND(AVG(P.salary), 2) AS avg_salary
FROM departments D
LEFT JOIN professors P ON
    D.dept_id = P.dept_id
GROUP BY D.dept_id
ORDER BY avg_salary;

-- 32. Find all departments where the total budget exceeds 600,000.
SELECT *
FROM departments
WHERE budget > 600000;

-- 33. Show the grade distribution for course CS101: count of each grade (A, B, C, D, F).
SELECT E.grade, COUNT(E.grade) AS total_students
FROM enrollments E
INNER JOIN courses C ON
    E.course_id = C.course_id
WHERE C.course_code = 'CS101'
GROUP BY E.grade;

-- 34. Using HAVING, list departments where more than 2 students are enrolled across all courses in that department.
SELECT dept_name, COUNT(E.enrollment_id) AS enrollments
FROM departments D
INNER JOIN courses C ON 
    D.dept_id = C.dept_id
INNER JOIN enrollments E ON
    C.course_id = E.course_id
GROUP BY D.dept_id
HAVING COUNT(E.enrollment_id) > 2

/* TASK 4 OUTPUT
college_db-# \i hands_on_2.sql
         course_name          | enrollment_count              
------------------------------+------------------
 Data Structures & Algorithms |                4
 Object Oriented Programming  |                2
 Circuit Theory               |                2
 Database Management Systems  |                2
 Thermodynamics               |                0
(5 rows)


    dept_name     | avg_salary                                
------------------+------------
 Civil            |   76000.00
 Mechanical       |   79000.00
 Electronics      |   82000.00
 Computer Science |   91500.00
(4 rows)


 dept_id |    dept_name     |   head_of_dept   |  budget      
---------+------------------+------------------+-----------
       1 | Computer Science | Dr. Ramesh Kumar | 850000.00
       2 | Electronics      | Dr. Priya Nair   | 620000.00
(2 rows)


 grade | total_students                                       
-------+----------------
 A     |              2
 B     |              2
(2 rows)


    dept_name     | enrollments                               
------------------+-------------
 Computer Science |           8
(1 row)
*/