# TASK 1 : Set Up Alembic and Create a Baseline Migration

# 92. In your project folder, run: alembic init migrations
# 93. Edit alembic.ini to set sqlalchemy.url to your college_db_orm connection string.
# 94. Edit migrations/env.py to import your models' Base and set target_metadata = Base.metadata.
# 95. Run alembic revision --autogenerate -m 'initial schema' to generate the first migration file.
# 96. Inspect the generated file in migrations/versions/ — confirm it contains the upgrade() and downgrade() functions.
# 97. Run alembic upgrade head to apply the migration. Verify the alembic_version table is created in your database.

""" TASK 1 OUTPUT
PS C:\Users\Rishab Sharma\Desktop\CognizantModule3_DatabaseIntegration\> alembic init migrations
Creating directory C:\Users\Rishab Sharma\Desktop\Cognizant\Module3_DatabaseIntegration\migrations ...  done
Creating directory C:\Users\Rishab Sharma\Desktop\Cognizant\Module3_DatabaseIntegration\migrations\versions ...  done
Generating C:\Users\Rishab Sharma\Desktop\Cognizant\Module3_DatabaseIntegration\alembic.ini ...  done
Generating C:\Users\Rishab Sharma\Desktop\Cognizant\Module3_DatabaseIntegration\migrations\env.py ...  done
Generating C:\Users\Rishab Sharma\Desktop\Cognizant\Module3_DatabaseIntegration\migrations\README ...  done
Generating C:\Users\Rishab Sharma\Desktop\Cognizant\Module3_DatabaseIntegration\migrations\script.py.mako ...  done
Please edit configuration/connection/logging settings in C:\Users\Rishab Sharma\Desktop\Cognizant\Module3_DatabaseIntegration\alembic.ini before proceeding.

`alembic.ini`
sqlalchemy.url = postgresql://postgres:310623104120@localhost:5433/college_db_orm

`migrations/env.py`
from models import Base
target_metadata = Base.metadata

PS C:\Users\Rishab Sharma\Desktop\Cognizant\Module3_DatabaseIntegration> alembic revision --autogenerate -m 'inital schema'
Creating engine : create_engine(DATABASE_URL, echo=True)
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.schemas
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.tables
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.types
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.constraints
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.defaults
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.comments
INFO  [alembic.ddl.postgresql] Detected sequence named 'courses_id_seq' as owned by integer column 'courses(id)', assuming SERIAL and omitting
INFO  [alembic.ddl.postgresql] Detected sequence named 'professors_id_seq' as owned by integer column 'professors(id)', assuming SERIAL and omitting
INFO  [alembic.ddl.postgresql] Detected sequence named 'students_id_seq' as owned by integer column 'students(id)', assuming SERIAL and omitting
INFO  [alembic.ddl.postgresql] Detected sequence named 'departments_id_seq' as owned by integer column 'departments(id)', assuming SERIAL and omitting
INFO  [alembic.ddl.postgresql] Detected sequence named 'enrollments_id_seq' as owned by integer column 'enrollments(id)', assuming SERIAL and omitting
Generating C:\Users\Rishab Sharma\Desktop\Cognizant\Module3_DatabaseIntegration\migrations\versions\b871a8485f18_inital_schema.py ...  done

`migrations\versions\b871a8485f18_inital_schema.py`
upgrade() & downgrade() exists

PS C:\Users\Rishab Sharma\Desktop\Cognizant\Module3_DatabaseIntegration> alembic upgrade head
Creating engine : create_engine(DATABASE_URL, echo=True)
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> b871a8485f18, inital schema

postgres=# \c college_db_orm
You are now connected to database "college_db_orm" as user "postgres".
college_db_orm=# \dt  
               List of tables                                                                                                                                              
 Schema |      Name       | Type  |  Owner   
--------+-----------------+-------+----------
 public | alembic_version | table | postgres
 public | courses         | table | postgres
 public | departments     | table | postgres
 public | enrollments     | table | postgres
 public | professors      | table | postgres
 public | students        | table | postgres
(6 rows)
"""

# TASK 2 : Add and Apply Incremental Migrations

# 98. In models.py, add a new column is_active BOOLEAN DEFAULT TRUE to the Student model.
# 99. Run alembic revision --autogenerate -m 'add is_active to students'.
# 100. Inspect the generated migration — confirm upgrade() adds the column and downgrade() drops it.
# 101. Apply with alembic upgrade head. Verify the column exists using your SQL client.
# 102. Add a new table CourseSchedule with columns: schedule_id, course_id (FK), day_of_week, start_time, end_time. Create the model, generate the migration, and apply it.
# 103. Run alembic history --verbose to see the full migration chain.

""" TASK 2 OUTPUT
from sqlalchemy import Boolean
class Student(Base):
    is_active = Column(Boolean, default=True, nullable=True)

PS C:\Users\Rishab Sharma\Desktop\Cognizant\Module3_DatabaseIntegration> alembic revision --autogenerate -m 'add is_active to students'
Creating engine : create_engine(DATABASE_URL, echo=True)
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.schemas
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.tables
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.types
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.constraints
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.defaults
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.comments
INFO  [alembic.ddl.postgresql] Detected sequence named 'departments_id_seq' as owned by integer column 'departments(id)', assuming SERIAL and omitting
INFO  [alembic.ddl.postgresql] Detected sequence named 'professors_id_seq' as owned by integer column 'professors(id)', assuming SERIAL and omitting
INFO  [alembic.ddl.postgresql] Detected sequence named 'enrollments_id_seq' as owned by integer column 'enrollments(id)', assuming SERIAL and omitting
INFO  [alembic.ddl.postgresql] Detected sequence named 'courses_id_seq' as owned by integer column 'courses(id)', assuming SERIAL and omitting
INFO  [alembic.ddl.postgresql] Detected sequence named 'students_id_seq' as owned by integer column 'students(id)', assuming SERIAL and omitting
INFO  [alembic.autogenerate.compare.tables] Detected added column 'students.is_active'

`migrations\versions\338d63e51969_add_is_active_to_students.py`
def upgrade() -> None:
    op.add_column('students', sa.Column('is_active', sa.Boolean(), nullable=True))
def downgrade() -> None:
    op.drop_column('students', 'is_active')

PS C:\Users\Rishab Sharma\Desktop\Cognizant\Module3_DatabaseIntegration> alembic upgrade head
Creating engine : create_engine(DATABASE_URL, echo=True)
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade b871a8485f18 -> 338d63e51969, add is_active to students

PS C:\Users\Rishab Sharma\Desktop\Cognizant\Module3_DatabaseIntegration> alembic revision --autogenerate -m 'add table CourseSchedule'
Creating engine : create_engine(DATABASE_URL, echo=True)
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.schemas
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.tables
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.types
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.constraints
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.defaults
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.comments
INFO  [alembic.autogenerate.compare.tables] Detected added table 'course_schedules'
INFO  [alembic.ddl.postgresql] Detected sequence named 'departments_id_seq' as owned by integer column 'departments(id)', assuming SERIAL and omitting
INFO  [alembic.ddl.postgresql] Detected sequence named 'professors_id_seq' as owned by integer column 'professors(id)', assuming SERIAL and omitting
INFO  [alembic.ddl.postgresql] Detected sequence named 'enrollments_id_seq' as owned by integer column 'enrollments(id)', assuming SERIAL and omitting
INFO  [alembic.ddl.postgresql] Detected sequence named 'students_id_seq' as owned by integer column 'students(id)', assuming SERIAL and omitting
INFO  [alembic.ddl.postgresql] Detected sequence named 'courses_id_seq' as owned by integer column 'courses(id)', assuming SERIAL and omitting
Generating C:\Users\Rishab Sharma\Desktop\Cognizant\Module3_DatabaseIntegration\migrations\versions\0311192b37c4_add_table_courseschedule.py ...  done

PS C:\Users\Rishab Sharma\Desktop\Cognizant\Module3_DatabaseIntegration> alembic upgrade head                           
Creating engine : create_engine(DATABASE_URL, echo=True)
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade 338d63e51969 -> 0311192b37c4, add table CourseSchedule

PS C:\Users\Rishab Sharma\Desktop\Cognizant\Module3_DatabaseIntegration> alembic history --verbose
Rev: 0311192b37c4 (head)
Parent: 338d63e51969
Path: C:\Users\Rishab Sharma\Desktop\Cognizant\Module3_DatabaseIntegration\migrations\versions\0311192b37c4_add_table_courseschedule.py

    add table CourseSchedule
    
    Revision ID: 0311192b37c4
    Revises: 338d63e51969
    Create Date: 2026-06-24 15:58:02.191609

Rev: 338d63e51969
Parent: b871a8485f18
Path: C:\Users\Rishab Sharma\Desktop\Cognizant\Module3_DatabaseIntegration\migrations\versions\338d63e51969_add_is_active_to_students.py

    add is_active to students
    
    Revision ID: 338d63e51969
    Revises: b871a8485f18
    Create Date: 2026-06-24 15:51:17.751338

Rev: b871a8485f18
Parent: <base>
Path: C:\Users\Rishab Sharma\Desktop\Cognizant\Module3_DatabaseIntegration\migrations\versions\b871a8485f18_inital_schema.py

    inital schema
    
    Revision ID: b871a8485f18
    Revises: 
    Create Date: 2026-06-24 15:36:11.435655
"""

# TASK 3 : Rollback and Recovery

# 104. Note the current alembic head revision hash using alembic current.
# 105. Roll back one step using alembic downgrade -1. Confirm the is_active column is dropped.
# 106. Roll back to the very first revision using alembic downgrade base (this undoes all migrations).
# 107. Re-apply all migrations with alembic upgrade head and confirm you are back to the latest state.

""" TASK 3 OUTPUT
PS C:\Users\Rishab Sharma\Desktop\Cognizant\Module3_DatabaseIntegration> alembic current
Creating engine : create_engine(DATABASE_URL, echo=True)
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
0311192b37c4 (head)

PS C:\Users\Rishab Sharma\Desktop\Cognizant\Module3_DatabaseIntegration> alembic downgrade -1
Creating engine : create_engine(DATABASE_URL, echo=True)
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running downgrade 0311192b37c4 -> 338d63e51969, add table CourseSchedule

PS C:\Users\Rishab Sharma\Desktop\Cognizant\Module3_DatabaseIntegration> alembic downgrade base          
Creating engine : create_engine(DATABASE_URL, echo=True)
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running downgrade 338d63e51969 -> b871a8485f18, add is_active to students
INFO  [alembic.runtime.migration] Running downgrade b871a8485f18 -> , inital schema

PS C:\Users\Rishab Sharma\Desktop\Cognizant\Module3_DatabaseIntegration> alembic upgrade head          
Creating engine : create_engine(DATABASE_URL, echo=True)
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> b871a8485f18, inital schema
INFO  [alembic.runtime.migration] Running upgrade b871a8485f18 -> 338d63e51969, add is_active to students
INFO  [alembic.runtime.migration] Running upgrade 338d63e51969 -> 0311192b37c4, add table CourseSchedule
"""
