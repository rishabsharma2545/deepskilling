# 57. Create main.py with: from fastapi import FastAPI; app = FastAPI(title='Course Management API', version='1.0'). 
# Add a root route @app.get('/') that returns {'message': 'API running'}.

# check `main.py`

# 58. Create schemas.py. Define Pydantic BaseModel classes: CourseCreate (name, code, credits, department_id), 
# CourseUpdate (all fields optional using Optional[]), CourseResponse (all fields plus id — this is the response schema).`

# 59. Define a DepartmentResponse schema that nests a list of CourseResponse objects to demonstrate Pydantic nested models.

# check `schemas.py` for 58 & 59

# 60. In main.py, add a POST /api/courses/ endpoint with signature: async def create_course(course: CourseCreate). 
# FastAPI automatically validates the request body against the Pydantic model and returns 422 if validation fails.

# 61. Visit http://127.0.0.1:8000/docs — observe the auto-generated Swagger UI showing your endpoints with request/response schemas.

# Visited and explored the localhost

# 62. Add a GET /api/courses/{course_id} endpoint. The path parameter course_id is automatically validated as an integer by FastAPI.

# 63. Add a GET /api/courses/ endpoint with optional query parameters: skip: int = 0, limit: int = 10, department_id: Optional[int] = None. 
# Use these to implement pagination and filtering.

# check `main.py`

# 64. Set up SQLAlchemy with an async engine using create_async_engine. 
# Define a get_db() dependency function that yields a database session.

# 65. Inject the database session into endpoints using FastAPI's Dependency Injection: 
# async def get_courses(db: AsyncSession = Depends(get_db)).

# 66. Implement the full CRUD for courses using async ORM queries: await db.execute(select(Course)), await db.commit(), etc.

# 67. Test pagination: GET /api/courses/?skip=0&limit=2 should return the first 2 courses; 
# GET /api/courses/?skip=2&limit=2 should return the next 2/