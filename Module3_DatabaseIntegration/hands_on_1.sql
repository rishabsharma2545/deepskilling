-- TASK 1 : Create the Database and Tables
-- executed `schema.sql` and `sample_data.sql` in postgres

/* TASK 1 OUTPUT
college_db=# \c college_db
You are now connected to database "college_db" as user "postgres".

college_db=# \i schema.sql
CREATE TYPE
CREATE TABLE
CREATE TABLE
CREATE TABLE
CREATE TABLE
CREATE TABLE

college_db=# \i sample_data.sql
INSERT 0 4
INSERT 0 8
INSERT 0 5
INSERT 0 12
INSERT 0 5 

college_db-# \dt
   List of tables  
 Schema |    Name| Type  |  Owner   
--------+-------------+-------+----------
 public | courses| table | postgres
 public | departments | table | postgres
 public | enrollments | table | postgres
 public | professors  | table | postgres
 public | students    | table | postgres
(5 rows)
*/

-- TASK 2 : Verify Normalisation
-- The schema satisfies 1NF, 2NF & 3NF

/* TASK 2 OUTPUT
1NF: 
Every column is storing only a single (atomic) value. 
There is no column where multiple values are stored in a single row.

2NF: 
Each table has a single-column primary key, and every non-key attribute 
depends entirely on that primary key. There are no partial dependencies.

3NF: 
Non-key attributes depend only on the primary key and not on other 
non-key attributes. Related information, such as department, student, 
and course details, is stored in separate tables, preventing transitive 
dependencies and reducing data redundancy.
*/

-- TASK 3 : Alter and Extend the Schema
-- executed `extension.sql` in postgres

/* TASK 3 OUTPUT
college_db-# \i extension.sql  
ALTER TABLE
ALTER TABLE
ALTER TABLE
ALTER TABLE

college_db-# \d courses
                                          Table "public.courses"  
   Column    |          Type          | Collation | Nullable |                  Default                   
-------------+------------------------+-----------+----------+--------------------------------------------
 course_id   | integer                |           | not null | nextval('courses_course_id_seq'::regclass)
 course_name | character varying(150) |           | not null | 
 course_code | character varying(20)  |           |          | 
 credits     | integer                |           |          | 
 dept_id     | integer                |           |          | 
 max_seats   | integer                |           |          | 60
Indexes:
    "courses_pkey" PRIMARY KEY, btree (course_id)
    "courses_course_code_key" UNIQUE CONSTRAINT, btree (course_code)
Foreign-key constraints:
    "courses_dept_id_fkey" FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
Referenced by:
    TABLE "enrollments" CONSTRAINT "enrollments_course_id_fkey" FOREIGN KEY (course_id) REFERENCES courses(course_id)

college_db-# \d departments
                                         Table "public.departments"                                     
    Column    |          Type          | Collation | Nullable |                   Default                    
--------------+------------------------+-----------+----------+----------------------------------------------
 dept_id      | integer                |           | not null | nextval('departments_dept_id_seq'::regclass)
 dept_name    | character varying(100) |           | not null | 
 head_of_dept | character varying(100) |           |          | 
 budget       | numeric(12,2)          |           |          | 
Indexes:
    "departments_pkey" PRIMARY KEY, btree (dept_id)
Referenced by:
    TABLE "courses" CONSTRAINT "courses_dept_id_fkey" FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
    TABLE "professors" CONSTRAINT "professors_dept_id_fkey" FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
    TABLE "students" CONSTRAINT "students_dept_id_fkey" FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
*/