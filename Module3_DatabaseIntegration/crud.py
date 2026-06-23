# 90. Compare the two outputs and document the difference in a comment block at the top of crud.py.
'''
1. N+1 PROBLEM:
   - Baseline query executed: `session.query(Enrollment).all()`
   - SQL logs emitted: 1 main query to fetch enrollment rows + 2 additional database roundtrips (1 for Student, 1 for Course) per row.
   - Total queries for 4 records: 1 + (4 * 2) = 9 total database hits.
   - Impact: Scales poorly. If the table grows to 1,000 rows, it hits the database 2,001 times.

2. EAGER LOADING:
   - Optimized query executed: `.options(joinedload(...))`
   - SQL logs emitted: Exactly 1 single complex query utilizing explicit SQL LEFT OUTER JOIN operations.
   - Total queries for 4 records: 1 total database read.
   - Impact: Highly efficient. Performance remains constant regardless of row volume.
'''

# 80. Create a crud.py file. Open a Session using sessionmaker.
from sqlalchemy.orm import sessionmaker
from models import engine, Department, Student, Course, Enrollment

Session = sessionmaker(bind=engine)
session = Session()

try:
    # 81. INSERT: Add 3 Department objects and 5 Student objects. Commit the session.
    print("\nAdd Departments")
    cs_dept = Department(name="Computer Science", code="CS")
    ee_dept = Department(name="Electrical Engineering", code="EE")
    ma_dept = Department(name="Mathematics", code="MA")
    
    session.add_all([cs_dept, ee_dept, ma_dept])
    session.flush()

    print("\nAdd Students")
    student1 = Student(name="Alice Smith", email="alice@univ.edu", admn_year=2023, department=cs_dept)
    student2 = Student(name="Bob Jones", email="bob@univ.edu", admn_year=2023, department=cs_dept)
    student3 = Student(name="Charlie Brown", email="charlie@univ.edu", admn_year=2022, department=ee_dept)
    student4 = Student(name="Diana Prince", email="diana@univ.edu", admn_year=2022, department=ee_dept)
    student5 = Student(name="Evan Wright", email="evan@univ.edu", admn_year=2023, department=ma_dept)

    session.add_all([student1, student2, student3, student4, student5])
    session.commit()
    print("Added Departments & Students")

    # 82. INSERT: Add 3 Course objects and 4 Enrollment objects linking students to courses.
    print("\nAdd Courses")
    cs101 = Course(course_code="CS101", title="Introduction to Programming", credits=4)
    cs102 = Course(course_code="CS102", title="Data Structures", credits=4)
    ee201 = Course(course_code="EE201", title="Circuit Analysis", credits=3)
    
    session.add_all([cs101, cs102, ee201])
    session.flush()

    print("\nAdd Enrollments")
    enroll1 = Enrollment(student=student1, course=cs101, semester="2022-ODD", grade="A")
    enroll2 = Enrollment(student=student2, course=cs101, semester="2022-ODD", grade="B")
    enroll3 = Enrollment(student=student1, course=cs102, semester="2023-EVEN", grade="A")
    enroll4 = Enrollment(student=student3, course=ee201, semester="2023-ODD", grade="B")

    session.add_all([enroll1, enroll2, enroll3, enroll4])
    session.commit()
    print("Added Courses & Enrollments")

    # 83. READ: Query all students in department 'Computer Science' using session.query(Student).join(Department).filter(Department.dept_name == 'Computer Science').
    print("\nFetch `Computer Science` students")
    cs_students = session.query(Student).join(Department).filter(Department.name == 'Computer Science').all()
    
    for student in cs_students:
        print(f" - Student Name: {student.name} (Email: {student.email})")

    # 84. READ: Query all enrollments and print each student's name alongside course name. Enable echo=True on the engine to count SQL queries issued.
    print("\nFetch all enrollments")
    
    # 87. Identify the N+1 query from Task 2 Step 5 by counting the SQL log lines with echo=True.
    session.bind.echo = True
    
    enrollments_baseline = session.query(Enrollment).all()
    
    for enroll in enrollments_baseline:
        print(f" - Student: {enroll.student.name : <25} | Course: {enroll.course.title : <100} | Semester: {enroll.semester : <10}")

    session.bind.echo = False

    # 88. Rewrite the query using joinedload:   from sqlalchemy.orm import joinedload session.query(Enrollment).options(joinedload(Enrollment.student), joinedload(Enrollment.course)).all()
    from sqlalchemy.orm import joinedload
    
    # 89. Count the SQL queries again with echo=True — it should now be 1 query (or 3 using the subquery loading strategy).
    session.bind.echo = True

    enrollments_optimized = (
        session.query(Enrollment).options(
            joinedload(Enrollment.student), joinedload(Enrollment.course)
        ).all()
    )
    
    for enroll in enrollments_optimized:
        print(f" -> Student: {enroll.student.name : <25} | Course: {enroll.course.title : <100}")
        
    session.bind.echo = False

    # 85. UPDATE: Find a specific student by email and update their admn_year. Commit.
    print("\nFind student by email and update admission year")
    mail_input = "alice@univ.edu"
    new_admn_year = 2022
    target_student = session.query(Student).filter(Student.email == mail_input).first()
    if target_student:
        target_student.admn_year = new_admn_year
        session.commit()
        print(f"Admission year updated successfully")

    # 86. DELETE: Remove an enrollment record using session.delete(enrollment_obj). Commit and verify.
    print("\nDelete enrollment record")
    enrollment_to_delete = session.query(Enrollment).filter_by(student_id=student2.id, course_id=cs101.id).first()
    
    if enrollment_to_delete:
        session.delete(enrollment_to_delete)
        session.commit()
        print("Enrollment deleted successfully")
        
        check_deleted = session.query(Enrollment).filter_by(student_id=student2.id, course_id=cs101.id).first()
        if check_deleted is None:
            print("Record no longer exists in the database")

except Exception as e:
    session.rollback()
    print(f"Transaction rolled back due to: {e}")
finally:
    session.close()
    print("\nSession expired")

