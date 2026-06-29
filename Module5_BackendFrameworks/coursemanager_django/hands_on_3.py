# 26. In courses/serializers.py, create a ModelSerializer for each model: 
# DepartmentSerializer, CourseSerializer, StudentSerializer, EnrollmentSerializer. Include all fields.

# check `serializers.py`

# 27. In courses/views.py, create a CourseListView using DRF's APIView: 
# handle GET (return all courses serialized) and POST (create a new course from request.data).

# 28. Create a CourseDetailView for GET (single course by pk), PUT (update), and DELETE operations.

# check `views.py` for 27 & 28

# 29. Wire both views in courses/urls.py: path('courses/', CourseListView.as_view()) and 
# path('courses/<int:pk>/', CourseDetailView.as_view()). Include courses/urls.py in the main urls.py.

# check `courses/urls.py` & `coursemanager_django/urls.py` 

# 30. Test all endpoints using Postman or Thunder Client: GET /api/courses/ should return a JSON list; 
# POST with a JSON body should create a course; DELETE /api/courses/id/ should remove it.

'''
1. GET /api/courses/

Request:
GET http://127.0.0.1:8000/api/courses/

Response:
HTTP 200 OK

[
    {
        "id": 1,
        "name": "Python Programming",
        "code": "CS101",
        "credits": 4,
        "department": 1
    },
    {
        "id": 2,
        "name": "Database Systems",
        "code": "CS102",
        "credits": 3,
        "department": 1
    },
    ...
]
-----------------------------------------------------

2. POST /api/courses/

Request:
POST http://127.0.0.1:8000/api/courses/

Headers:
Content-Type: application/json

Body:
{
    "name": "Machine Learning",
    "code": "CS111",
    "credits": 4,
    "department": 1
}

Response:
HTTP 201 Created

{
    "id": 12,
    "name": "Machine Learning",
    "code": "CS111",
    "credits": 4,
    "department": 1
}
-----------------------------------------------------

3. GET /api/courses/12/

Request:
GET http://127.0.0.1:8000/api/courses/12/

Response:
HTTP 200 OK

{
    "id": 12,
    "name": "Machine Learning",
    "code": "CS111",
    "credits": 4,
    "department": 1
}
-----------------------------------------------------

4. PUT /api/courses/12/

Request:
PUT http://127.0.0.1:8000/api/courses/12/

Headers:
Content-Type: application/json

Body:
{
    "name": "Advanced Machine Learning",
    "code": "CS111",
    "credits": 5,
    "department": 1
}

Response:
HTTP 200 OK

{
    "id": 12,
    "name": "Advanced Machine Learning",
    "code": "CS450",
    "credits": 5,
    "department": 1
}
-----------------------------------------------------

5. DELETE /api/courses/12/

Request:
DELETE http://127.0.0.1:8000/api/courses/12/

Response:
HTTP 204 No Content
-----------------------------------------------------

6. Verify Deletion

Request:
GET http://127.0.0.1:8000/api/courses/12/

Response:
HTTP 404 Not Found

{
    "error": "Course not found"
}
-----------------------------------------------------
'''

# 31. Replace CourseListView and CourseDetailView with a single CourseViewSet that extends viewsets.ModelViewSet. 
# This gives you all 5 CRUD operations with just 3 lines of code.

# check `views.py`

# 32. Create a DefaultRouter in courses/urls.py and register the viewset: router.register('courses', CourseViewSet). 
# Include router.urls. Observe how the router auto-generates all URL patterns.

# check `courses/urls.py`

# 33. Do the same for StudentViewSet and EnrollmentViewSet.

# check `views.py`

# 34. Add a custom action to CourseViewSet using the @action decorator: 
# a GET endpoint /api/courses/{id}/students/ that returns all students enrolled in that course.

# check `views.py`

# 35. Test the custom action endpoint in Postman. 
# Verify it returns only students enrolled in the specified course.

'''
GET /api/courses/1/students/
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 1,
        "first_name": "Rahul",
        "last_name": "Sharma",
        "email": "rahul@example.com",
        "enrollment_year": 2024,
        "department": 1
    },
    {
        "id": 2,
        "first_name": "Priya",
        "last_name": "Verma",
        "email": "priya@example.com",
        "enrollment_year": 2024,
        "department": 1
    }
]
'''