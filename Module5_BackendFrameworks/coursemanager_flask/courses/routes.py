# 39. In courses/routes.py, define a Blueprint: courses_bp = Blueprint('courses', __name__, url_prefix='/api/courses'). 
# Add route handlers for GET / and POST /.

from flask import jsonify, request
from courses import courses_bp

# 44. Create a helper function make_response_json(data, status_code) that always returns a consistent 
# JSON envelope: {'status': 'success', 'data': data}.
def make_response_json(data, status_code=200, status_str='success'):
    response = {'status': status_str, 'data': data}
    return jsonify(response), status_code

COURSES = {
    1: {"id": 1, "name": "AIML", "code": "CS101", "credits": 4},
    2: {"id": 2, "name": "DBMS", "code": "CS202", "credits": 3}
}

@courses_bp.route('/', methods=['GET'])
def get_courses():
    return jsonify([])

@courses_bp.route('/', methods=['POST'])
def create_course():
    data = request.get_json() or {}

    # 42. In the POST / route, use request.get_json() to parse the request body. 
    # Validate that required fields are present — return 400 with an error message if any are missing.
    required_fields = ['name', 'code', 'credits']
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        return make_response_json(
            data={"error": f"Missing required fields: {missing_fields}"},
            status_code=400, status_str='fail'
        )

    new_id = max(COURSES.keys()) + 1 if COURSES else 1
    new_course = {
        "id": new_id,
        "name": data['name'],
        "code": data['code'],
        "credits": data['credits']
    }
    COURSES[new_id] = new_course

    return make_response_json(new_course, 201)      

# 43. Add GET /<int:course_id>/ route, PUT /<int:course_id>/ route, DELETE /<int:course_id>/ routes in the blueprint.
@courses_bp.route('/<int:course_id>/', methods=['GET'])
def get_course(course_id):
    course = COURSES.get(course_id)
    if not course:
        return make_response_json({"error": "Course not found"}, 404, 'fail')
    return make_response_json(course, 200)

@courses_bp.route('/<int:course_id>/', methods=['PUT'])
def update_course(course_id):
    if course_id not in COURSES:
        return make_response_json({"error": "Course not found"}, 404, 'fail')
        
    data = request.get_json() or {}
    course = COURSES[course_id]
    
    course['name'] = data.get('name', course['name'])
    course['code'] = data.get('code', course['code'])
    course['credits'] = data.get('credits', course['credits'])
    
    return make_response_json(course, 200)

@courses_bp.route('/<int:course_id>/', methods=['DELETE'])
def delete_course(course_id):
    if course_id not in COURSES:
        return make_response_json({"error": "Course not found"}, 404, 'fail')
        
    deleted_course = COURSES.pop(course_id)
    return make_response_json({"message": f"Course {course_id} deleted", "course": deleted_course}, 200)