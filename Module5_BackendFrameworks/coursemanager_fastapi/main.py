# 57. Create main.py with: from fastapi import FastAPI; app = FastAPI(title='Course Management API', version='1.0'). 
# Add a root route @app.get('/') that returns {'message': 'API running'}.

from contextlib import asynccontextmanager
from typing import List, Optional
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import engine, Base, get_db
from models import Course
from schemas import CourseCreate, CourseUpdate, CourseResponse

# Create database tables automatically on startup (convenient for development)
@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(title='The Course Manager', version='1.0', lifespan=lifespan)

# 65 & 66. Implement Asynchronous CRUD endpoints

@app.post('/api/courses/', response_model=CourseResponse, status_code=status.HTTP_201_CREATED)
async def create_course(course: CourseCreate, db: AsyncSession = Depends(get_db)):
    db_course = Course(**course.model_dump())
    db.add(db_course)
    await db.commit()
    await db.refresh(db_course)
    return db_course


# 63 & 67. GET /api/courses/ with explicit pagination and filtering limits
@app.get('/api/courses/', response_model=List[CourseResponse])
async def get_courses(
    skip: int = 0, 
    limit: int = 10, 
    department_id: Optional[int] = None, 
    db: AsyncSession = Depends(get_db)
):
    stmt = select(Course)
    if department_id is not None:
        stmt = stmt.where(Course.department_id == department_id)
    
    # Apply pagination offsets
    stmt = stmt.offset(skip).limit(limit)
    
    result = await db.execute(stmt)
    return result.scalars().all()


@app.get('/api/courses/{course_id}', response_model=CourseResponse)
async def get_course(course_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Course).where(Course.id == course_id))
    db_course = result.scalar_one_or_none()
    if not db_course:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_course


@app.put('/api/courses/{course_id}', response_model=CourseResponse)
async def update_course(course_id: int, course_data: CourseUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Course).where(Course.id == course_id))
    db_course = result.scalar_one_or_none()
    if not db_course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    # Update only the attributes provided in the request body
    update_data = course_data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_course, key, value)
        
    await db.commit()
    await db.refresh(db_course)
    return db_course


@app.delete('/api/courses/{course_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_course(course_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Course).where(Course.id == course_id))
    db_course = result.scalar_one_or_none()
    if not db_course:
        raise HTTPException(status_code=404, detail="Course not found")
        
    await db.delete(db_course)
    await db.commit()
    return None