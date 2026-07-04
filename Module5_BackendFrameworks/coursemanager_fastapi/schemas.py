# 58. Create schemas.py. Define Pydantic BaseModel classes: CourseCreate (name, code, credits, department_id), 
# CourseUpdate (all fields optional using Optional[]), CourseResponse (all fields plus id — this is the response schema).

from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

class CourseCreate(BaseModel):
    name: str
    code: str
    credits: int
    department_id: int

class CourseUpdate(BaseModel):
    name: Optional[str] = None
    code: Optional[int] = None
    credits: Optional[int] = None
    department_id: Optional[int] = None

class CourseResponse(BaseModel):
    id: int
    name: str
    code: int
    credits: int
    department_id: int

    class Config:
        from_attributes = True

# 59. Define a DepartmentResponse schema that nests a list of CourseResponse objects to demonstrate Pydantic nested models.
class DepartmentResponse(BaseModel):
    department_id: int
    department_name: str
    course_responses: List[CourseResponse]

    class Config:
        from_attributes = True

class StudentCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr

class StudentUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None

class StudentResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    class Config:
        from_attributes = True

class EnrollmentCreate(BaseModel):
    student_id: int
    course_id: int

class EnrollmentUpdate(BaseModel):
    student_id: Optional[int] = None
    course_id: Optional[int] = None

class EnrollmentResponse(BaseModel):
    id: int
    student_id: int
    course_id: int
    enrollment_date: datetime
    class Config:
        from_attributes = True

# User schemas
class UserRegister(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    is_active: bool

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
