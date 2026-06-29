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