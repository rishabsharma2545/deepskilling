# 47. In app.py, initialise Flask-SQLAlchemy: db = SQLAlchemy(). In create_app(), call db.init_app(app).

# check `app.py`

# 48. In courses/models.py, define Department, Course, Student, and Enrollment SQLAlchemy models 
# using db.Model as the base. Mirror the same schema used in the Django hands-on.

# 49. Define relationships: Course has a db.relationship('Department', back_populates='courses'). 
# Enrollment has relationships to both Student and Course.

# check `models.py` for 48 & 49

# 50. Initialise Flask-Migrate: migrate = Migrate(app, db). 
# Run flask db init, flask db migrate -m 'initial schema', flask db upgrade. Verify tables are created.

'''
PS C:\Users\Rishab Sharma\Desktop\Cognizant\Module5_BackendFrameworks\coursemanager_flask> python -m flask db init
Creating directory C:\Users\Rishab Sharma\Desktop\Cognizant\Module5_BackendFrameworks\coursemanager_flask\migrations ...  done
Creating directory C:\Users\Rishab Sharma\Desktop\Cognizant\Module5_BackendFrameworks\coursemanager_flask\migrations\versions ...  done
Generating C:\Users\Rishab Sharma\Desktop\Cognizant\Module5_BackendFrameworks\coursemanager_flask\migrations\alembic.ini ...  done
Generating C:\Users\Rishab Sharma\Desktop\Cognizant\Module5_BackendFrameworks\coursemanager_flask\migrations\env.py ...  done
Generating C:\Users\Rishab Sharma\Desktop\Cognizant\Module5_BackendFrameworks\coursemanager_flask\migrations\README ...  done
Generating C:\Users\Rishab Sharma\Desktop\Cognizant\Module5_BackendFrameworks\coursemanager_flask\migrations\script.py.mako ...  done
Please edit configuration/connection/logging settings in C:\Users\Rishab Sharma\Desktop\Cognizant\Module5_BackendFrameworks\coursemanager_flask\migrations\alembic.ini before proceeding.

PS C:\Users\Rishab Sharma\Desktop\Cognizant\Module5_BackendFrameworks\coursemanager_flask> python -m flask db migrate -m "Initial schema"
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.schemas
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.tables
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.types
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.constraints
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.defaults
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.comments
INFO  [alembic.autogenerate.compare.tables] Detected added table 'departments'
INFO  [alembic.autogenerate.compare.tables] Detected added table 'students'
INFO  [alembic.autogenerate.compare.tables] Detected added table 'courses'
INFO  [alembic.autogenerate.compare.tables] Detected added table 'enrollments'
Generating C:\Users\Rishab Sharma\Desktop\Cognizant\Module5_BackendFrameworks\coursemanager_flask\migrations\versions\2f634e631e32_initial_schema.py ...  done

PS C:\Users\Rishab Sharma\Desktop\Cognizant\Module5_BackendFrameworks\coursemanager_flask> python -m flask db upgrade                    
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> 2f634e631e32, Initial schema
'''

# 51. Use the Flask shell (flask shell) to insert 2 departments and 3 courses via the ORM. 
# Commit using db.session.commit().

'''
> python -m flask shell
Ctrl click to launch VS Code Native REPL
Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
App: app
Instance: C:\Users\Rishab Sharma\Desktop\Cognizant\Module5_BackendFrameworks\coursemanager_flask\instance
>>> from app import db
>>> from courses.models import Department, Course
>>> cs_dept = Department(name="Computer Science", code="CS")
>>> math_dept = Department(name="Mathematics", code="MATH")
>>> db.session.add_all([cs_dept, math_dept])
>>> db.session.commit()
>>> course1 = Course(title="Introduction to Programming", code="CS101", department=cs_dept)
>>> course2 = Course(title="Data Structures", code="CS201", department=cs_dept)
>>> course3 = Course(title="Linear Algebra", code="MATH301", department=math_dept)
>>> db.session.add_all([course1, course2, course3])
>>> db.session.commit()
>>> print(Course.query.all())
[<Course CS101>, <Course CS201>, <Course MATH301>]
>>> print(Department.query.all())
[<Department CS>, <Department MATH>]
'''

# 52. Update the GET /api/courses/ route to query the database: Course.query.all() (or
# db.session.execute(db.select(Course)).scalars()). Serialise results to a list of dicts using a to_dict() method on the model.

# 53. Add a to_dict() method to each model that returns a dictionary of its fields — 
# this is Flask's equivalent of DRF serializers.

# 54. Update POST /api/courses/ to create a Course object, add it to the session, and commit. 
# Return the new course as JSON with status 201.

# 55. Update GET /<int:id>/, PUT, and DELETE to use Course.query.get_or_404(id) — 
# this automatically returns a 404 JSON response if the course is not found.

# 56. Add a route GET /api/courses/<int:id>/students/ that uses a JOIN query to return all students enrolled in the specified course.

# check `routes.py` for 52, 54, 55 & 56

# check `models.py` for 53
