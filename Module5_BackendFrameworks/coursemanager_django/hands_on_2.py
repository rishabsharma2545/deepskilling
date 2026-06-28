# 11. In courses/models.py, define the following models: Department, Course, Student, Enrollment

# 12. Add __str__ methods to each model returning a human-readable string.

# refer `models.py` for 11 & 12

# 13. Run python manage.py makemigrations to generate the migration files. 
# Inspect the generated migration file — identify the CreateTable operations.

'''
> python manage.py makemigrations
Migrations for 'courses':
  courses\migrations\0001_initial.py
    + Create model Department
    + Create model Course
    + Create model Student
    + Create model Enrollment
'''

# 14. Run python manage.py migrate to apply migrations. 
# Confirm the tables exist by checking the database with python manage.py dbshell.

'''
> python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, courses, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying courses.0001_initial... OK
  Applying sessions.0001_initial... OK

> python manage.py dbshell
SQLite version 3.46.0 2024-05-23 13:25:27 (UTF-16 console I/O)
Enter ".help" for usage hints.
sqlite> .tables
auth_group                  courses_department        
auth_group_permissions      courses_enrollment        
auth_permission             courses_student           
auth_user                   django_admin_log          
auth_user_groups            django_content_type       
auth_user_user_permissions  django_migrations         
courses_course              django_session 
'''

# 15. Add a Meta class to the Enrollment model with unique_together = [['student','course']] to prevent duplicate enrollments.

'''
> python manage.py makemigrations
Migrations for 'courses':
  courses\migrations\0002_alter_enrollment_unique_together.py
    ~ Alter unique_together for enrollment (1 constraint(s))

> python manage.py migrate       
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, courses, sessions
Running migrations:
  Applying courses.0002_alter_enrollment_unique_together... OK
'''

# 16. Open the Django shell with python manage.py shell. 
# Create at least 2 Department, 4 Course, and 5 Student objects using Model.objects.create(...).

'''
>>> from courses.models import Department, Course, Student
>>> cse = Department.objects.create(name = "CSE", head_of_dept = "Cloudin", budget = 5000000)
>>> ece = Department.objects.create(name = "ECE", head_of_dept = "Kanimozhi", budget = 3500000)
>>> Department.objects.all()
<QuerySet [<Department: CSE>, <Department: ECE>]>

>>> Course.objects.create(name="Python Programming", code="CS101", credits=4, department=cse)
<Course: CS101 - Python Programming>
>>> Course.objects.create(name="Database Systems", code="CS102", credits=3, department=cse)
<Course: CS102 - Database Systems>
>>> Course.objects.create(name="Digital Electronics", code="EC101", credits=4, department=ece)
<Course: EC101 - Digital Electronics>
>>> Course.objects.create(name="Microprocessors", code="EC102", credits=3, department=ece)
<Course: EC102 - Microprocessors>
>>> Course.objects.all()
<QuerySet [<Course: CS101 - Python Programming>, <Course: CS102 - Database Systems>, <Course: EC101 - Digital Electronics>, <Course: EC102 - Microprocessors>]>

>>> Student.objects.create( first_name="Rahul", last_name="Sharma", email="rahul@example.com", department=cse, enrollment_year=2024)
<Student: Rahul Sharma>
>>> Student.objects.create( first_name="Priya", last_name="Verma", email="priya@example.com", department=cse, enrollment_year=2024)
<Student: Priya Verma>
>>> Student.objects.create( first_name="Arjun", last_name="Singh", email="arjun@example.com", department=ece, enrollment_year=2023)
<Student: Arjun Singh>
>>> Student.objects.create( first_name="Sneha", last_name="Patel", email="sneha@example.com", department=ece, enrollment_year=2022)
<Student: Sneha Patel>
>>> Student.objects.create( first_name="Neha", last_name="Gupta", email="neha@example.com", department=cse, enrollment_year=2025)
<Student: Neha Gupta>
>>> Student.objects.all()
<QuerySet [<Student: Rahul Sharma>, <Student: Priya Verma>, <Student: Arjun Singh>, <Student: Sneha Patel>, <Student: Neha Gupta>]>
'''

# 17. Query all courses in a specific department using Course.objects.filter(department__name='CSE'). 
# Note the double underscore — this is a Django ORM lookup across a ForeignKey.

'''
>>> Course.objects.filter(department__name = 'CSE')
<QuerySet [<Course: CS101 - Python Programming>, <Course: CS102 - Database Systems>]>
'''

# 18. Use .values() and .annotate() to count the number of courses per department: 
# Department.objects.annotate(course_count=Count('course')).

'''
>>> Department.objects.values("name").annotate(course_count = Count("courses"))
<QuerySet [{'name': 'CSE', 'course_count': 2}, {'name': 'ECE', 'course_count': 2}]>

'''

# 19. Use select_related to fetch all students along with their department in a single SQL query. 
# Confirm with Django's connection.queries log.

'''
>>> from django.db import connection, reset_queries
>>> 
>>> reset_queries()
>>> 
>>> students = Student.objects.select_related("department")
>>> 
>>> for student in students:
...     print(student.first_name, student.department.name)
... 
Rahul CSE
Priya CSE
Arjun ECE
Sneha ECE
Neha CSE
>>> print(len(connection.queries))
1
'''

# 20. Perform an update: increase the budget of all departments by 10% using Department.objects.update(budget=F('budget') * 1.1).

'''
>>> from django.db.models import F
>>> Department.objects.values("name", "budget")
<QuerySet [{'name': 'CSE', 'budget': Decimal('5000000.00')}, {'name': 'ECE', 'budget': Decimal('3500000.00')}]>
>>> Department.objects.update(budget = F("budget") * 1.1)
2
>>> Department.objects.values("name", "budget")          
<QuerySet [{'name': 'CSE', 'budget': Decimal('5500000.00')}, {'name': 'ECE', 'budget': Decimal('3850000.00')}]>
'''

# 21. Create a superuser: python manage.py createsuperuser. 
# Use admin / admin@college.edu / Admin@123 for local testing.

'''
> python manage.py createsuperuser
Username (leave blank to use 'rishabsharma'): admin
Email address: admin@college.edu
Password: *********
Password (again): *********
Superuser created successfully.
'''

# 22. In courses/admin.py, register all four models. 
# Start the server and explore the admin at /admin/.

# 23. Customise the CourseAdmin: use list_display = ['name','code','credits','department'] to 
# show multiple columns in the list view. Add search_fields = ['name','code'] to enable search.

# 24. Add list_filter = ['department'] to CourseAdmin to enable sidebar filtering by department.

# refer `admin.py` for 22, 23, 24

# 25. Create 3 courses, 5 students, and 4 enrollments through the admin interface. 
# Verify the unique_together constraint on Enrollment by trying to enroll a duplicate entry.

# Created 3 courses, 5 students, 4 enrollments through the dashboard