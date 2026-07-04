# 78. Review all your existing endpoints. Identify and fix any violations of REST resource naming: 
# URLs should use nouns not verbs, should be plural, and should use hyphens not underscores for multi-word resources.

# 79. Verify HTTP methods are semantically correct: GET (read), POST (create), PUT (full replace), PATCH (partial update), DELETE (remove). 
# Add a PATCH /api/courses/{id}/ endpoint for partial updates alongside the existing PUT.
    
# 80. Verify status codes: 200 OK for GET/PUT/PATCH, 201 Created for POST (with a Location header pointing to the new resource), 204 No Content for DELETE, 
# 400 Bad Request for validation errors, 401 Unauthorised for missing auth, 404 Not Found, 422 Unprocessable Entity for schema errors.
    
# 81. Add a Location response header to all POST endpoints: response.headers['Location'] = f'/api/courses/{new_course.id}/'.

# 82. Add versioning to your API URLs: change /api/courses/ to /api/v1/courses/. Discuss (in a code comment) two alternative versioning strategies: 
# URL versioning vs header-based versioning (Accept: application/vnd.api+json;version=1).

'''
1. URL Versioning
   Example:
   /api/v1/courses/

   Advantages:
   - Simple and easy to understand
   - Visible in the URL
   - Easy to test with browsers and Postman

2. Header-Based Versioning
   Example:
   Accept: application/vnd.api+json;version=1

   Advantages:
   - Keeps URLs clean
   - Clients choose the API version through HTTP headers
   - Suitable for large enterprise APIs
'''

# 83. Implement offset pagination on GET /api/v1/courses/: accept page and page_size query params. 
# Return a response envelope: {'count': total, 'next': url_or_null, 'previous': url_or_null, 'results': [...]}. 

# 84. Add a filtering query parameter search= to GET /api/v1/courses/ that searches course name and code with a case-insensitive LIKE query.

# 85. Standardise all error responses to follow the format: {'error': {'code': 'NOT_FOUND', 'message': 'Course with id 99 does not exist', 'field': null}}. 
# Update all error handlers to use this format.