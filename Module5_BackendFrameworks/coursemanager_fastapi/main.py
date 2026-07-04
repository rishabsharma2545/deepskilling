import asyncio
from contextlib import asynccontextmanager
from typing import List, Optional
from fastapi import FastAPI, Depends, HTTPException, status, BackgroundTasks, Response, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from sqlalchemy import select, func, or_
from sqlalchemy.ext.asyncio import AsyncSession

from database import engine, Base, get_db
from models import Course, Student, Enrollment, User
from security import get_password_hash, verify_password, create_access_token
from schemas import (
    CourseCreate, CourseUpdate, CourseResponse,
    StudentCreate, StudentUpdate, StudentResponse,
    EnrollmentCreate, EnrollmentUpdate, EnrollmentResponse,
    UserRegister, UserResponse, UserLogin, Token
)

from fastapi.middleware.cors import CORSMiddleware

# 92. Create a get_current_user(token: str = Depends(oauth2_scheme)) dependency that decodes and validates the JWT token, returning the current user object. 
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from security import SECRET_KEY, ALGORITHM
oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "/api/v1/auth/login/")

async def get_current_user(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    result = await db.execute(select(User).where(User.email == email))
    user = result.scalar_one_or_none()

    if user is None:
        raise credentials_exception

    return user

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
    lifespan = lifespan,
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

# 94. Configure CORS in your app to allow requests from http://localhost:3000 (your frontend dev server). 
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:3000"], allow_credentials = True,
    allow_methods = ["*"], allow_headers = ["*"],
)

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "code": "NOT_FOUND" if exc.status_code == 404 else "HTTP_ERROR",
                "message": exc.detail,
                "field": None
            }
        }
    )


@app.get('/', include_in_schema=False)
def home():
    return {'message': 'API running'}


# COURSE ENDPOINTS (76, 77)
# 77. Add descriptive summary and response_description metadata to the decorator
@app.post(
    '/api/v1/courses/', 
    response_model=CourseResponse, 
    status_code=status.HTTP_201_CREATED,
    tags=['Courses'],
    summary="Create a new course entry",
    response_description="The course record was successfully validated and committed to the storage layer."
)
async def create_course(course: CourseCreate, response: Response, current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    db_course = Course(**course.model_dump())
    db.add(db_course)
    await db.commit()
    await db.refresh(db_course)
    
    # 81. Add a Location response header to all POST endpoints
    response.headers["Location"] = f"/api/v1/courses/{db_course.id}"
    return db_course


# 76. Group operations seamlessly using Swagger documentation tags

# 83. Implement offset pagination on GET /api/v1/courses/: accept page and page_size query params. 
@app.get('/api/v1/courses/', response_model=List[CourseResponse], tags=['Courses'])
async def get_courses(page: int = 1, page_size: int = 10, department_id: Optional[int] = None, search: Optional[str] = None, db: AsyncSession = Depends(get_db)):
    offset = (page - 1) * page_size

    stmt = select(Course)

    if department_id is not None:
        stmt = stmt.where(Course.department_id == department_id)

    # 84. Add a filtering query parameter search= to GET /api/v1/courses/ that searches course name and code with a case-insensitive LIKE query.
    if search:
        stmt = stmt.where(
            or_(Course.name.ilike(f"%{search}%"), Course.code.ilike(f"%{search}%"))
        )

    count_stmt = select(func.count()).select_from(stmt.subquery())
    total = await db.scalar(count_stmt)

    result = await db.execute(stmt.offset(offset).limit(page_size))
    courses = result.scalars().all()

    next_url = (
        f"/api/v1/courses/?page={page+1}&page_size={page_size}"
        if offset + page_size < total
        else None
    )

    previous_url = (
        f"/api/v1/courses/?page={page-1}&page_size={page_size}"
        if page > 1
        else None
    )

    # 83. Return a response envelope: {'count': total, 'next': url_or_null, 'previous': url_or_null, 'results': [...]}. 
    return {
        "count": total,
        "next": next_url,
        "previous": previous_url,
        "results": courses
    }

@app.get('/api/v1/courses/{course_id}', response_model=CourseResponse, tags=['Courses'])
async def get_course(course_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Course).where(Course.id == course_id))
    db_course = result.scalar_one_or_none()
    if not db_course:
        raise HTTPException(status_code=404, detail='Course not found')
    return db_course


@app.put('/api/v1/courses/{course_id}', response_model=CourseResponse, tags=['Courses'])
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

# 79. Add a PATCH /api/courses/{id}/ endpoint for partial updates alongside the existing PUT.
@app.patch("/api/v1/courses/{course_id}", response_model=CourseResponse, tags=["Courses"])
async def patch_course(course_id: int, course_data: CourseUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Course).where(Course.id == course_id))
    db_course = result.scalar_one_or_none()

    if not db_course:
        raise HTTPException(status_code=404, detail="Course not found")

    update_data = course_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_course, key, value)

    await db.commit()
    await db.refresh(db_course)
    return db_course

@app.delete('/api/v1/courses/{course_id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Courses'])
async def delete_course(course_id: int, current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Course).where(Course.id == course_id))
    db_course = result.scalar_one_or_none()
    if not db_course:
        raise HTTPException(status_code=404, detail='Course not found')
    await db.delete(db_course)
    await db.commit()
    return None


@app.get('/api/v1/courses/{course_id}/students/', response_model=List[StudentResponse], tags=['Courses'])
async def get_course_students(course_id: int, db: AsyncSession = Depends(get_db)):
    course_check = await db.execute(select(Course).where(Course.id == course_id))
    if not course_check.scalar_one_or_none():
        raise HTTPException(status_code=404, detail='Course not found')

    stmt = select(Student).join(Enrollment, Student.id == Enrollment.student_id).where(Enrollment.course_id == course_id)
    result = await db.execute(stmt)
    return result.scalars().all()


# STUDENT ENDPOINTS (76)
@app.post('/api/v1/students/', response_model=StudentResponse, status_code=status.HTTP_201_CREATED, tags=['Students'])
async def create_student(student: StudentCreate, response: Response, db: AsyncSession = Depends(get_db)):
    db_student = Student(**student.model_dump())
    db.add(db_student)
    await db.commit()
    await db.refresh(db_student)
    # 81. Add a Location response header to all POST endpoints
    response.headers["Location"] = f"/api/v1/students/{db_student.id}"
    return db_student


@app.get('/api/v1/students/', response_model=List[StudentResponse], tags=['Students'])
async def get_students(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Student).offset(skip).limit(limit))
    return result.scalars().all()


@app.get('/api/v1/students/{student_id}', response_model=StudentResponse, tags=['Students'])
async def get_student(student_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Student).where(Student.id == student_id))
    db_student = result.scalar_one_or_none()
    if not db_student:
        raise HTTPException(status_code=404, detail='Student not found')
    return db_student


@app.put('/api/v1/students/{student_id}', response_model=StudentResponse, tags=['Students'])
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


@app.delete('/api/v1/students/{student_id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Students'])
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
@app.post('/api/v1/enrollments/', response_model=EnrollmentResponse, status_code=status.HTTP_201_CREATED, tags=['Enrollments'])
async def create_enrollment(
    enrollment: EnrollmentCreate, response: Response,
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
    # 81. Add a Location response header to all POST endpoints
    response.headers["Location"] = f"/api/v1/enrollments/{db_enrollment.id}"

    # Register our asynchronous email confirmation dispatch inside the background runtime array
    background_tasks.add_task(send_enrollment_email, db_student.email, db_course.code)
    
    return db_enrollment


@app.get('/api/v1/enrollments/', response_model=List[EnrollmentResponse], tags=['Enrollments'])
async def get_enrollments(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Enrollment).offset(skip).limit(limit))
    return result.scalars().all()


@app.get('/api/v1/enrollments/{enrollment_id}', response_model=EnrollmentResponse, tags=['Enrollments'])
async def get_enrollment(enrollment_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Enrollment).where(Enrollment.id == enrollment_id))
    db_enrollment = result.scalar_one_or_none()
    if not db_enrollment:
        raise HTTPException(status_code=404, detail='Enrollment not found')
    return db_enrollment


@app.put('/api/v1/enrollments/{enrollment_id}', response_model=EnrollmentResponse, tags=['Enrollments'])
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


@app.delete('/api/v1/enrollments/{enrollment_id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Enrollments'])
async def delete_enrollment(enrollment_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Enrollment).where(Enrollment.id == enrollment_id))
    db_enrollment = result.scalar_one_or_none()
    if not db_enrollment:
        raise HTTPException(status_code=404, detail='Enrollment not found')
    await db.delete(db_enrollment)
    await db.commit()
    return None

# 88. Create a POST /api/v1/auth/register/ endpoint that: validates the email format, checks the email is not already registered (return 409 Conflict if so), 
# hashes the password using get_password_hash, and saves the user.
@app.post("/api/v1/auth/register/", response_model = UserResponse, status_code = status.HTTP_201_CREATED, tags = ["Authentication"])
async def register_user(user: UserRegister, response: Response, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.email == user.email))
    existing_user = result.scalar_one_or_none()

    if existing_user:
        raise HTTPException(status_code = status.HTTP_409_CONFLICT, detail = "Email already registered")
    
    secured_password = get_password_hash(user.password)

    db_user = User(email = user.email, hashed_password = secured_password, is_active = True)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)

    response.headers["Location"] = f"/api/v1/auth/users/{db_user.id}"

    return db_user

# LOGIN ENDPOINT
# 91. Create a POST /api/v1/auth/login/ endpoint that: accepts email and password, verifies credentials using verify_password
@app.post("/api/v1/auth/login/", response_model=Token, tags=["Authentication"])
async def login(user: UserLogin, db: AsyncSession = Depends(get_db)):

    result = await db.execute(select(User).where(User.email == user.email))
    db_user = result.scalar_one_or_none()

    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")

    # Create JWT
    access_token = create_access_token(data={"sub": db_user.email})
    return {"access_token": access_token, "token_type": "bearer"}
