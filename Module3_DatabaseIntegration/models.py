# 75. Create a Python file models.py. Import necessary classes from sqlalchemy.
import os
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean, Time, Float, DateTime
from sqlalchemy.orm import declarative_base, relationship

# 76. Define an engine connecting to your college_db PostgreSQL database.
DATABASE_URL = "postgresql://postgres:310623104120@localhost:5433/college_db_orm"

print('Creating engine : create_engine(DATABASE_URL, echo=True)')
engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()

# 77. Define five ORM model classes: Department, Student, Course, Enrollment, Professor — mapping to the same columns as your SQL schema.
class Department(Base):
    __tablename__ = 'departments'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    code = Column(String(10), nullable=False, unique=True)
    
    # 78. Define relationships: Student has a many-to-one relationship to Department. Enrollment has many-to-one relationships to both Student and Course.
    students = relationship("Student", back_populates="department")


class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    admn_year = Column(Integer, nullable=False)
    department_id = Column(Integer, ForeignKey('departments.id'), nullable=False)
    is_active = Column(Boolean, default=True, nullable=True)
    
    # 78. Define relationships: Student has a many-to-one relationship to Department. Enrollment has many-to-one relationships to both Student and Course.
    department = relationship("Department", back_populates="students")
    enrollments = relationship("Enrollment", back_populates="student")


class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True)
    course_code = Column(String(10), nullable=False, unique=True)
    title = Column(String(100), nullable=False)
    credits = Column(Integer, nullable=False, default=3)
    
    # 78. Define relationships: Student has a many-to-one relationship to Department. Enrollment has many-to-one relationships to both Student and Course.
    enrollments = relationship("Enrollment", back_populates="course")


class Enrollment(Base):
    __tablename__ = 'enrollments'
    
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)
    semester = Column(String(15), nullable=False)  # e.g., '2022-ODD'
    grade = Column(String(2), nullable=True)        # e.g., 'A', 'B'
    
    # 78. Relationships: Enrollment acts as join table for Student and Course
    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")


class Professor(Base):
    __tablename__ = 'professors'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    specialization = Column(String(100), nullable=True)

class CourseSchedule(Base):
    __tablename__ = 'course_schedules'
    
    schedule_id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)
    day_of_week = Column(String(15), nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    
    course = relationship("Course")

# 79. Use Base.metadata.create_all(engine) to auto-create tables in a fresh database (college_db_orm), and confirm they appear in your SQL client.
if __name__ == "__main__":
    print("Creating tables in college_db_orm: Base.metadata.create_all(engine)")
    Base.metadata.create_all(engine)
    print("Tables created successfully!")