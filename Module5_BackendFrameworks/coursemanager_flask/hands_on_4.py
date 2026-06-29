# 36. Create a project folder flask_coursemanager/. Inside, create: app.py, config.py 
# and a courses/ package with __init__.py and routes.py.

''' CREATED
coursemanager_flask/
    |
    |---courses/
    |      |---`__init__.py`
    |      |---`routes.py`
    |
    |---`app.py`
    |---`config.py`
'''

# 37. In app.py, create the Flask app using the application factory pattern.

# check `app.py`

# 38. In config.py, define a Config class with SQLALCHEMY_DATABASE_URI, SECRET_KEY, and DEBUG settings.

# check `config.py`

# 39. In courses/routes.py, define a Blueprint: courses_bp = Blueprint('courses', __name__, url_prefix='/api/courses'). 
# Add route handlers for GET / and POST /.

# check `routes.py`

# 40. Register the blueprint in create_app() with app.register_blueprint(courses_bp).

# check `app.py`

# 41. Run the app and test that GET /api/courses/ returns a JSON response using jsonify([]).

'''
http://127.0.0.1:5000/api/courses/
[]
'''

# 42. In the POST / route, use request.get_json() to parse the request body. 
# Validate that required fields are present — return 400 with an error message if any are missing.

# 43. Add GET /<int:course_id>/ route, PUT /<int:course_id>/ route, DELETE /<int:course_id>/ routes in the blueprint.

# 44. Create a helper function make_response_json(data, status_code) that always returns a consistent 
# JSON envelope: {'status': 'success', 'data': data}.

# check `routes.py`

# 45. Add Flask error handlers for 404 and 500 using @app.errorhandler(404). 
# Return JSON error responses (not HTML) — APIs should never return HTML error pages.

# check `app.py`

# 46. Use Postman to test all endpoints. Verify that missing fields return 400, 
# unknown IDs return 404, and successful operations return 200 or 201.

# verified the status