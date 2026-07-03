import asyncio
from contextlib import asynccontextmanager
from typing import List, Optional
from fastapi import FastAPI, Depends, HTTPException, status, BackgroundTasks
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import engine, Base, get_db
from models import Course, Student, Enrollment
from schemas import (
    CourseCreate, CourseUpdate, CourseResponse,
    StudentCreate, StudentUpdate, StudentResponse,
    EnrollmentCreate, EnrollmentUpdate, EnrollmentResponse
)

# 73. Task function to simulate asynchronous background work
async def send_enrollment_email(student_email: str, course_code: str):
    print(f"[BACKGROUND TASK STARTING] Preparing email stream for {student_email}...")
    # Simulate an actual delay time like networking or SMTP connection handling
    await asyncio.sleep(4) 
    print(f"[BACKGROUND TASK SUCCESS] Confirmation email successfully sent to {student_email} for course {course_code}!")


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


# 75. Customize structural OpenAPI metadata directly inside the constructor instance
app = FastAPI(
    title="University Course Management API",
    description=(
        "An advanced relational REST API engine designed to handle university course catalogs, "
        "student listings, and concurrent enrollment tracking asynchronously using FastAPI and SQLAlchemy."
    ),
    version="2.1.0",
    contact={
        "name": "Academic IT Support Team",
        "url": "https://example.com/support",
        "email": "it-support@university.edu",
    }
)

@app.get('/', include_in_schema=False)
def home():
    return {'message': 'API running'}


# COURSE ENDPOINTS (76, 77)
# 77. Add descriptive summary and response_description metadata to the decorator
@app.post(
    '/api/courses/', 
    response_model=CourseResponse, 
    status_code=status.HTTP_201_CREATED,
    tags=['Courses'],
    summary="Create a new course entry",
    response_description="The course record was successfully validated and committed to the storage layer."
)
async def create_course(course: CourseCreate, db: AsyncSession = Depends(get_db)):
    db_course = Course(**course.model_dump())
    db.add(db_course)
    await db.commit()
    await db.refresh(db_course)
    return db_course


# 76. Group operations seamlessly using Swagger documentation tags
@app.get('/api/courses/', response_model=List[CourseResponse], tags=['Courses'])
async def get_courses(skip: int = 0, limit: int = 10, department_id: Optional[int] = None, db: AsyncSession = Depends(get_db)):
    stmt = select(Course)
    if department_id is not None:
        stmt = stmt.where(Course.department_id == department_id)
    result = await db.execute(stmt.offset(skip).limit(limit))
    return result.scalars().all()


@app.get('/api/courses/{course_id}', response_model=CourseResponse, tags=['Courses'])
async def get_course(course_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Course).where(Course.id == course_id))
    db_course = result.scalar_one_or_none()
    if not db_course:
        raise HTTPException(status_code=404, detail='Course not found')
    return db_course


@app.put('/api/courses/{course_id}', response_model=CourseResponse, tags=['Courses'])
async def update_course(course_id: int, course_data: CourseUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Course).where(Course.id == course_id))
    db_course = result.scalar_one_or_none()
    if not db_course:
        raise HTTPException(status_code=404, detail='Course not found')
    
    update_data = course_data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_course, key, value)
    await db.commit()
    await db.refresh(db_course)
    return db_course


@app.delete('/api/courses/{course_id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Courses'])
async def delete_course(course_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Course).where(Course.id == course_id))
    db_course = result.scalar_one_or_none()
    if not db_course:
        raise HTTPException(status_code=404, detail='Course not found')
    await db.delete(db_course)
    await db.commit()
    return None


@app.get('/api/courses/{course_id}/students/', response_model=List[StudentResponse], tags=['Courses'])
async def get_course_students(course_id: int, db: AsyncSession = Depends(get_db)):
    course_check = await db.execute(select(Course).where(Course.id == course_id))
    if not course_check.scalar_one_or_none():
        raise HTTPException(status_code=404, detail='Course not found')

    stmt = select(Student).join(Enrollment, Student.id == Enrollment.student_id).where(Enrollment.course_id == course_id)
    result = await db.execute(stmt)
    return result.scalars().all()


# STUDENT ENDPOINTS (76)
@app.post('/api/students/', response_model=StudentResponse, status_code=status.HTTP_201_CREATED, tags=['Students'])
async def create_student(student: StudentCreate, db: AsyncSession = Depends(get_db)):
    db_student = Student(**student.model_dump())
    db.add(db_student)
    await db.commit()
    await db.refresh(db_student)
    return db_student


@app.get('/api/students/', response_model=List[StudentResponse], tags=['Students'])
async def get_students(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Student).offset(skip).limit(limit))
    return result.scalars().all()


@app.get('/api/students/{student_id}', response_model=StudentResponse, tags=['Students'])
async def get_student(student_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Student).where(Student.id == student_id))
    db_student = result.scalar_one_or_none()
    if not db_student:
        raise HTTPException(status_code=404, detail='Student not found')
    return db_student


@app.put('/api/students/{student_id}', response_model=StudentResponse, tags=['Students'])
async def update_student(student_id: int, student_data: StudentUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Student).where(Student.id == student_id))
    db_student = result.scalar_one_or_none()
    if not db_student:
        raise HTTPException(status_code=404, detail='Student not found')
    
    update_data = student_data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_student, key, value)
    await db.commit()
    await db.refresh(db_student)
    return db_student


@app.delete('/api/students/{student_id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Students'])
async def delete_student(student_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Student).where(Student.id == student_id))
    db_student = result.scalar_one_or_none()
    if not db_student:
        raise HTTPException(status_code=404, detail='Student not found')
    await db.delete(db_student)
    await db.commit()
    return None


# ENROLLMENT ENDPOINTS (73, 76)
# 73. Add BackgroundTasks interface parameter configuration directly to the request signature
@app.post('/api/enrollments/', response_model=EnrollmentResponse, status_code=status.HTTP_201_CREATED, tags=['Enrollments'])
async def create_enrollment(
    enrollment: EnrollmentCreate, 
    background_tasks: BackgroundTasks, 
    db: AsyncSession = Depends(get_db)
):
    student_query = await db.execute(select(Student).where(Student.id == enrollment.student_id))
    db_student = student_query.scalar_one_or_none()
    
    course_query = await db.execute(select(Course).where(Course.id == enrollment.course_id))
    db_course = course_query.scalar_one_or_none()
    
    if not db_student:
        raise HTTPException(status_code=404, detail='Student not found')
    if not db_course:
        raise HTTPException(status_code=404, detail='Course not found')

    db_enrollment = Enrollment(**enrollment.model_dump())
    db.add(db_enrollment)
    await db.commit()
    await db.refresh(db_enrollment)

    # Register our asynchronous email confirmation dispatch inside the background runtime array
    background_tasks.add_task(send_enrollment_email, db_student.email, db_course.code)
    
    return db_enrollment


@app.get('/api/enrollments/', response_model=List[EnrollmentResponse], tags=['Enrollments'])
async def get_enrollments(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Enrollment).offset(skip).limit(limit))
    return result.scalars().all()


@app.get('/api/enrollments/{enrollment_id}', response_model=EnrollmentResponse, tags=['Enrollments'])
async def get_enrollment(enrollment_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Enrollment).where(Enrollment.id == enrollment_id))
    db_enrollment = result.scalar_one_or_none()
    if not db_enrollment:
        raise HTTPException(status_code=404, detail='Enrollment not found')
    return db_enrollment


@app.put('/api/enrollments/{enrollment_id}', response_model=EnrollmentResponse, tags=['Enrollments'])
async def update_enrollment(enrollment_id: int, enrollment_data: EnrollmentUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Enrollment).where(Enrollment.id == enrollment_id))
    db_enrollment = result.scalar_one_or_none()
    if not db_enrollment:
        raise HTTPException(status_code=404, detail='Enrollment not found')
        
    update_data = enrollment_data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_enrollment, key, value)
    await db.commit()
    await db.refresh(db_enrollment)
    return db_enrollment


@app.delete('/api/enrollments/{enrollment_id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Enrollments'])
async def delete_enrollment(enrollment_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Enrollment).where(Enrollment.id == enrollment_id))
    db_enrollment = result.scalar_one_or_none()
    if not db_enrollment:
        raise HTTPException(status_code=404, detail='Enrollment not found')
    await db.delete(db_enrollment)
    await db.commit()
    return None