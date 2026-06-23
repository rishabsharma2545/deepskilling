# TASK 1 : SQLAlchemy — Define Models and Connect

# 75. Create a Python file models.py. Import necessary classes from sqlalchemy.
# 76. Define an engine connecting to your college_db PostgreSQL database.
# 77. Define five ORM model classes: Department, Student, Course, Enrollment, Professor — mapping to the same columns as your SQL schema.
# 78. Define relationships: Student has a many-to-one relationship to Department. Enrollment has many-to-one relationships to both Student and Course.
# 79. Use Base.metadata.create_all(engine) to auto-create tables in a fresh database (college_db_orm), and confirm they appear in your SQL client.

""" TASK 1 OUTPUT
Creating engine : create_engine(DATABASE_URL, echo=True)
Creating tables in college_db_orm: Base.metadata.create_all(engine)
2026-06-24 02:18:28,455 INFO sqlalchemy.engine.Engine select pg_catalog.version()
2026-06-24 02:18:28,455 INFO sqlalchemy.engine.Engine [raw sql] {}
2026-06-24 02:18:28,456 INFO sqlalchemy.engine.Engine select current_schema()
2026-06-24 02:18:28,456 INFO sqlalchemy.engine.Engine [raw sql] {}
2026-06-24 02:18:28,457 INFO sqlalchemy.engine.Engine show standard_conforming_strings
2026-06-24 02:18:28,457 INFO sqlalchemy.engine.Engine [raw sql] {}
2026-06-24 02:18:28,458 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2026-06-24 02:18:28,460 INFO sqlalchemy.engine.Engine SELECT pg_catalog.pg_class.relname 
FROM pg_catalog.pg_class JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_class.relnamespace 
WHERE pg_catalog.pg_class.relname = %(table_name)s AND pg_catalog.pg_class.relkind = ANY (ARRAY[%(param_1)s, %(param_2)s, %(param_3)s, %(param_4)s, %(param_5)s]) AND pg_catalog.pg_table_is_visible(pg_catalog.pg_class.oid) AND pg_catalog.pg_namespace.nspname != %(nspname_1)s
2026-06-24 02:18:28,461 INFO sqlalchemy.engine.Engine [generated in 0.00031s] {'table_name': 'departments', 'param_1': 'r', 'param_2': 'p', 'param_3': 'f', 'param_4': 'v', 'param_5': 'm', 'nspname_1': 'pg_catalog'}
2026-06-24 02:18:28,466 INFO sqlalchemy.engine.Engine SELECT pg_catalog.pg_class.relname 
FROM pg_catalog.pg_class JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_class.relnamespace 
WHERE pg_catalog.pg_class.relname = %(table_name)s AND pg_catalog.pg_class.relkind = ANY (ARRAY[%(param_1)s, %(param_2)s, %(param_3)s, %(param_4)s, %(param_5)s]) AND pg_catalog.pg_table_is_visible(pg_catalog.pg_class.oid) AND pg_catalog.pg_namespace.nspname != %(nspname_1)s
2026-06-24 02:18:28,466 INFO sqlalchemy.engine.Engine [cached since 0.005805s ago] {'table_name': 'students', 'param_1': 'r', 'param_2': 'p', 'param_3': 'f', 'param_4': 'v', 'param_5': 'm', 'nspname_1': 'pg_catalog'}
2026-06-24 02:18:28,468 INFO sqlalchemy.engine.Engine SELECT pg_catalog.pg_class.relname 
FROM pg_catalog.pg_class JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_class.relnamespace 
WHERE pg_catalog.pg_class.relname = %(table_name)s AND pg_catalog.pg_class.relkind = ANY (ARRAY[%(param_1)s, %(param_2)s, %(param_3)s, %(param_4)s, %(param_5)s]) AND pg_catalog.pg_table_is_visible(pg_catalog.pg_class.oid) AND pg_catalog.pg_namespace.nspname != %(nspname_1)s
2026-06-24 02:18:28,468 INFO sqlalchemy.engine.Engine [cached since 0.007722s ago] {'table_name': 'courses', 'param_1': 'r', 'param_2': 'p', 'param_3': 'f', 'param_4': 'v', 'param_5': 'm', 'nspname_1': 'pg_catalog'}
2026-06-24 02:18:28,471 INFO sqlalchemy.engine.Engine SELECT pg_catalog.pg_class.relname 
FROM pg_catalog.pg_class JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_class.relnamespace 
WHERE pg_catalog.pg_class.relname = %(table_name)s AND pg_catalog.pg_class.relkind = ANY (ARRAY[%(param_1)s, %(param_2)s, %(param_3)s, %(param_4)s, %(param_5)s]) AND pg_catalog.pg_table_is_visible(pg_catalog.pg_class.oid) AND pg_catalog.pg_namespace.nspname != %(nspname_1)s
2026-06-24 02:18:28,471 INFO sqlalchemy.engine.Engine [cached since 0.01053s ago] {'table_name': 'enrollments', 'param_1': 'r', 'param_2': 'p', 'param_3': 'f', 'param_4': 'v', 'param_5': 'm', 'nspname_1': 'pg_catalog'}
2026-06-24 02:18:28,473 INFO sqlalchemy.engine.Engine SELECT pg_catalog.pg_class.relname 
FROM pg_catalog.pg_class JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_class.relnamespace 
WHERE pg_catalog.pg_class.relname = %(table_name)s AND pg_catalog.pg_class.relkind = ANY (ARRAY[%(param_1)s, %(param_2)s, %(param_3)s, %(param_4)s, %(param_5)s]) AND pg_catalog.pg_table_is_visible(pg_catalog.pg_class.oid) AND pg_catalog.pg_namespace.nspname != %(nspname_1)s
2026-06-24 02:18:28,473 INFO sqlalchemy.engine.Engine [cached since 0.01276s ago] {'table_name': 'professors', 'param_1': 'r', 'param_2': 'p', 'param_3': 'f', 'param_4': 'v', 'param_5': 'm', 'nspname_1': 'pg_catalog'}
2026-06-24 02:18:28,476 INFO sqlalchemy.engine.Engine 
CREATE TABLE departments (
        id SERIAL NOT NULL, 
        name VARCHAR(100) NOT NULL, 
        code VARCHAR(10) NOT NULL, 
        PRIMARY KEY (id), 
        UNIQUE (name), 
        UNIQUE (code)
)


2026-06-24 02:18:28,476 INFO sqlalchemy.engine.Engine [no key 0.00040s] {}
2026-06-24 02:18:28,658 INFO sqlalchemy.engine.Engine 
CREATE TABLE courses (
        id SERIAL NOT NULL, 
        course_code VARCHAR(10) NOT NULL, 
        title VARCHAR(100) NOT NULL, 
        credits INTEGER NOT NULL, 
        PRIMARY KEY (id), 
        UNIQUE (course_code)
)


2026-06-24 02:18:28,659 INFO sqlalchemy.engine.Engine [no key 0.00068s] {}
2026-06-24 02:18:28,672 INFO sqlalchemy.engine.Engine 
CREATE TABLE professors (
        id SERIAL NOT NULL, 
        name VARCHAR(100) NOT NULL, 
        email VARCHAR(100) NOT NULL, 
        specialization VARCHAR(100), 
        PRIMARY KEY (id), 
        UNIQUE (email)
)


2026-06-24 02:18:28,672 INFO sqlalchemy.engine.Engine [no key 0.00053s] {}
2026-06-24 02:18:28,682 INFO sqlalchemy.engine.Engine 
CREATE TABLE students (
        id SERIAL NOT NULL, 
        name VARCHAR(100) NOT NULL, 
        email VARCHAR(100) NOT NULL, 
        admn_year INTEGER NOT NULL, 
        department_id INTEGER NOT NULL, 
        PRIMARY KEY (id), 
        UNIQUE (email), 
        FOREIGN KEY(department_id) REFERENCES departments (id)
)


2026-06-24 02:18:28,683 INFO sqlalchemy.engine.Engine [no key 0.00099s] {}
2026-06-24 02:18:28,697 INFO sqlalchemy.engine.Engine 
CREATE TABLE enrollments (
        id SERIAL NOT NULL, 
        student_id INTEGER NOT NULL, 
        course_id INTEGER NOT NULL, 
        semester VARCHAR(15) NOT NULL, 
        grade VARCHAR(2), 
        PRIMARY KEY (id), 
        FOREIGN KEY(student_id) REFERENCES students (id), 
        FOREIGN KEY(course_id) REFERENCES courses (id)
)


2026-06-24 02:18:28,697 INFO sqlalchemy.engine.Engine [no key 0.00031s] {}
2026-06-24 02:18:28,712 INFO sqlalchemy.engine.Engine COMMIT
Tables created successfully!
"""

# TASK 2 : CRUD Operations via ORM

# 80. Create a crud.py file. Open a Session using sessionmaker.
# 81. INSERT: Add 3 Department objects and 5 Student objects. Commit the session.
# 82. INSERT: Add 3 Course objects and 4 Enrollment objects linking students to courses.
# 83. READ: Query all students in department 'Computer Science' using session.query(Student).join(Department).filter(Department.dept_name == 'Computer Science').
# 84. READ: Query all enrollments and print each student's name alongside course name. Enable echo=True on the engine to count SQL queries issued.
# 85. UPDATE: Find a specific student by email and update their enrollment_year. Commit.
# 86. DELETE: Remove an enrollment record using session.delete(enrollment_obj). Commit and verify.

""" TASK 2 OUTPUT
Creating engine : create_engine(DATABASE_URL, echo=True)

Add Departments

Add Students
Added Departments & Students

Add Courses

Add Enrollments
Added Courses & Enrollments

Fetch `Computer Science` students
 - Student Name: Alice Smith (Email: alice@univ.edu)
 - Student Name: Bob Jones (Email: bob@univ.edu)

Fetch all enrollments
 - Student: Alice Smith   | Course: Introduction to Programming      | Semester: 2022-ODD  
 - Student: Bob Jones     | Course: Introduction to Programming      | Semester: 2022-ODD  
 - Student: Alice Smith   | Course: Data Structures      | Semester: 2023-EVEN 
 - Student: Charlie Brown | Course: Circuit Analysis     | Semester: 2023-ODD  
 -> Student: Alice Smith   | Course: Introduction to Programming     
 -> Student: Bob Jones     | Course: Introduction to Programming     
 -> Student: Alice Smith   | Course: Data Structures     
 -> Student: Charlie Brown | Course: Circuit Analysis    

Find student by email and update admission year
Admission year updated successfully

Delete enrollment record
Enrollment deleted successfully
Record no longer exists in the database

Session expired
"""

# TASK 3 : Eager Loading to Fix N+1

# 87. Identify the N+1 query from Task 2 Step 5 by counting the SQL log lines with echo=True.
# 88. Rewrite the query using joinedload:   from sqlalchemy.orm import joinedload session.query(Enrollment).options(joinedload(Enrollment.student), joinedload(Enrollment.course)).all()
# 89. Count the SQL queries again with echo=True — it should now be 1 query (or 3 using the subquery loading strategy).
# 90. Compare the two outputs and document the difference in a comment block at the top of crud.py.

""" TASK 3 OUTPUT
2026-06-24 02:19:31,380 INFO sqlalchemy.engine.Engine SELECT enrollments.id AS enrollments_id, enrollments.student_id AS enrollments_student_id, enrollments.course_id AS enrollments_course_id, enrollments.semester AS enrollments_semester, enrollments.grade AS enrollments_grade 
FROM enrollments
2026-06-24 02:19:31,380 INFO sqlalchemy.engine.Engine [generated in 0.00061s] {}

2026-06-24 02:19:31,385 INFO sqlalchemy.engine.Engine SELECT courses.id AS courses_id, courses.course_code AS courses_course_code, courses.title AS courses_title, courses.credits AS courses_credits 
FROM courses 
WHERE courses.id = %(pk_1)s
2026-06-24 02:19:31,386 INFO sqlalchemy.engine.Engine [generated in 0.00080s] {'pk_1': 1}
 - Student: Alice Smith   | Course: Introduction to Programming      | Semester: 2022-ODD  
 - Student: Bob Jones     | Course: Introduction to Programming      | Semester: 2022-ODD  

2026-06-24 02:19:31,390 INFO sqlalchemy.engine.Engine SELECT courses.id AS courses_id, courses.course_code AS courses_course_code, courses.title AS courses_title, courses.credits AS courses_credits 
FROM courses 
WHERE courses.id = %(pk_1)s
2026-06-24 02:19:31,391 INFO sqlalchemy.engine.Engine [cached since 0.005761s ago] {'pk_1': 2}
 - Student: Alice Smith   | Course: Data Structures      | Semester: 2023-EVEN 

2026-06-24 02:19:31,396 INFO sqlalchemy.engine.Engine SELECT students.id AS students_id, students.name AS students_name, students.email AS students_email, students.admn_year AS students_admn_year, students.department_id AS students_department_id 
FROM students 
WHERE students.id = %(pk_1)s
2026-06-24 02:19:31,396 INFO sqlalchemy.engine.Engine [generated in 0.00051s] {'pk_1': 3}

2026-06-24 02:19:31,398 INFO sqlalchemy.engine.Engine SELECT courses.id AS courses_id, courses.course_code AS courses_course_code, courses.title AS courses_title, courses.credits AS courses_credits 
FROM courses 
WHERE courses.id = %(pk_1)s
2026-06-24 02:19:31,399 INFO sqlalchemy.engine.Engine [cached since 0.01395s ago] {'pk_1': 3}
 - Student: Charlie Brown | Course: Circuit Analysis     | Semester: 2023-ODD

 
2026-06-24 02:19:31,407 INFO sqlalchemy.engine.Engine SELECT enrollments.id AS enrollments_id, enrollments.student_id AS enrollments_student_id, enrollments.course_id AS enrollments_course_id, enrollments.semester AS enrollments_semester, enrollments.grade AS enrollments_grade, students_1.id AS students_1_id, students_1.name AS students_1_name, students_1.email AS students_1_email, students_1.admn_year AS students_1_admn_year, students_1.department_id AS students_1_department_id, courses_1.id AS courses_1_id, courses_1.course_code AS courses_1_course_code, courses_1.title AS courses_1_title, courses_1.credits AS courses_1_credits 
FROM enrollments LEFT OUTER JOIN students AS students_1 ON students_1.id = enrollments.student_id LEFT OUTER JOIN courses AS courses_1 ON courses_1.id = enrollments.course_id
2026-06-24 02:19:31,407 INFO sqlalchemy.engine.Engine [generated in 0.00048s] {}
 -> Student: Alice Smith   | Course: Introduction to Programming     
 -> Student: Bob Jones     | Course: Introduction to Programming     
 -> Student: Alice Smith   | Course: Data Structures     
 -> Student: Charlie Brown | Course: Circuit Analysis
"""

