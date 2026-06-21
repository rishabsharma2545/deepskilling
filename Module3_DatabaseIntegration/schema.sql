CREATE TYPE GRADE_SCALE AS ENUM ('A', 'B', 'C', 'D', 'F');

CREATE TABLE departments(
    dept_id SERIAL PRIMARY KEY,
    dept_name VARCHAR(100) NOT NULL,
    hod_name VARCHAR(100),
    budget DECIMAL(12,2)
);

CREATE TABLE students(
    student_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    date_of_birth DATE,
    dept_id INT REFERENCES departments(dept_id),
    enrollment_year INT
);

CREATE TABLE courses(
    course_id SERIAL PRIMARY KEY, 
    course_name VARCHAR(150) NOT NULL,
    course_code VARCHAR(20) UNIQUE,
    credits INT,
    dept_id INT REFERENCES departments(dept_id)
);

CREATE TABLE enrollments(
    enrollment_id SERIAL PRIMARY KEY, 
    student_id INT REFERENCES students(student_id),
    course_id INT REFERENCES courses(course_id),
    enrollment_date DATE,
    grade GRADE_SCALE
);

CREATE TABLE professors(
    professor_id SERIAL PRIMARY KEY, 
    prof_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    dept_id INT REFERENCES departments(dept_id),
    salary DECIMAL(10,2)
);