# 1. Describe the journey of a GET /api/courses/ request through a Django application:
# URL router → View → Model (DB query) → Response.

'''
1. A client sends a GET request to /api/courses/.
2. The request reaches Django through a WSGI or ASGI server.
3. Middleware processes the incoming request.
4. Django matches the URL in urls.py and routes it to the appropriate view.
5. The view handles the request and queries the Model using Django ORM.
6. The ORM translates the query into SQL, retrieves data from the database, and returns model objects.
7. In Django REST Framework, a serializer converts the model objects into JSON.
8. The view returns an HTTP Response (usually 200 OK).
9. The response passes through middleware again before being sent back to the client.
'''


# 2. Identify where middleware sits in this cycle. Name two built-in Django middleware
# classes and describe what each does.

'''
Middleware sits between the web server and the view. It runs before the request reaches
the view and again before the response is sent back.

Examples:
- AuthenticationMiddleware: Identifies the logged-in user and makes it available as request.user.
- SecurityMiddleware: Adds security headers and can redirect HTTP requests to HTTPS.
'''


# 3. Explain the difference between WSGI and ASGI. State which one Django uses by default
# and when you would switch to ASGI.

'''
WSGI (Web Server Gateway Interface):
- Handles synchronous HTTP requests.
- Best for traditional Django applications.

ASGI (Asynchronous Server Gateway Interface):
- Supports asynchronous requests, async views, WebSockets, and long-lived connections.
- Better for real-time applications such as chat or live notifications.

Django supports both WSGI and ASGI. Traditional deployments typically use WSGI, while
ASGI is preferred when asynchronous features or high concurrency are required.
'''


# 4. Explain the MVC pattern, then map it to Django's MVT (Model-View-Template):
# what does each letter correspond to in Django?

'''
MVC (Model-View-Controller):
- Model: Handles data and business logic.
- View: Displays data to the user.
- Controller: Handles requests and coordinates between the Model and View.

Django follows the MVT pattern:
- Model: Same as the MVC Model.
- View: Acts like the MVC Controller by handling requests and business logic.
- Template: Acts like the MVC View by displaying data to the user.

Mapping:
MVC Model      → Django Model
MVC View       → Django Template
MVC Controller → Django View
'''

# 5. Run django-admin startproject coursemanager to create the project. 
# Inspect the generated files: settings.py, urls.py, wsgi.py, asgi.py.
'''
* coursemanager_django/settings.py
    - defines the project root, installed apps, middlewares, databases, etc

* coursemanager_django/urls.py
    - defines the paths of API endpoints of the app

* coursemanager_django/wsgi.py
    - web server gateway interface for sending synchronous requests

* coursemanager_django/asgi.py
    - asynchronous server gateway interface for sending asynchronous requests
'''

# 6. Run python manage.py startapp courses to create a Django app inside the project. 
# Differentiate between a Django project and a Django app.

'''
a Django project represents the entire web application, while 
a Django app is a self-contained submodule that handles a single specific feature
'''