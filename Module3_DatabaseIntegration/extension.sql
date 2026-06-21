-- Task 3 - 10
ALTER TABLE students 
ADD COLUMN phone_number VARCHAR(15);

-- Task 3 - 11
ALTER TABLE courses
ADD COLUMN max_seats INT DEFAULT 60;

-- Task 3 - 12
-- Already implemented using GRADE_SCALE enum

-- Task 3 - 13
ALTER TABLE departments
RENAME COLUMN hod_name
TO head_of_dept;

-- Task 4 - 14
ALTER TABLE students
DROP COLUMN phone_number;
