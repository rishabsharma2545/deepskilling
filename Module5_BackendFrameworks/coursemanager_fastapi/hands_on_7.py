# 68. Complete PUT /api/courses/{id} and DELETE /api/courses/{id}. 
# Use response_model=CourseResponse on GET and POST endpoints to document and validate the response shape.

# 69. Use status_code=status.HTTP_201_CREATED on the POST endpoint and status_code=status.HTTP_204_NO_CONTENT on DELETE.

# 70. Use HTTPException(status_code=404, detail='Course not found') when a course ID does not exist. 
# FastAPI converts this to a JSON error response automatically.

# 71. Add a GET /api/courses/{id}/students/ endpoint that returns all students enrolled in the course, using a JOIN query.

# 72. Implement all CRUD for Students and Enrollments following the same patterns.
    
# 73. Add a BackgroundTasks parameter to the POST /api/enrollments/ endpoint. 
# After creating an enrollment, add a background task that simulates sending a confirmation email.

# 74. Verify the endpoint returns immediately (201) without waiting for the background task — 
# check the server console for the print output after the response.
    
# 75. Customise the OpenAPI metadata in the FastAPI() constructor: add title, description, version, and contact information.

# 76. Add tags to group related endpoints: @app.get('/api/courses/', tags=['Courses']). 
# Observe how the Swagger UI organises endpoints by tag.

# 77. Add response_description and summary to the @app.post decorator for the create course endpoint. 
# Check how this appears in the /docs UI.

# check `models.py` -> `schemas.py` -> `main.py`