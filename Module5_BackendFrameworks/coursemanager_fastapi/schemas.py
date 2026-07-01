# 58. Create schemas.py. Define Pydantic BaseModel classes: CourseCreate (name, code, credits, department_id), 
# CourseUpdate (all fields optional using Optional[]), CourseResponse (all fields plus id — this is the response schema).

from pydantic import BaseModel
from typing import Optional, List

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

