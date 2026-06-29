# 39. In courses/routes.py, define a Blueprint: courses_bp = Blueprint('courses', __name__, url_prefix='/api/courses'). 
# Add route handlers for GET / and POST /.

from flask import jsonify, request
from courses import courses_bp

@courses_bp.route('/', methods=['GET'])
def get_course():
    return jsonify([])

@courses_bp.route('/', methods=['POST'])
def create_course():
    data = request.get_json() or {}

    return jsonify({
        "message": "Course created successfully",
        "data": data
    }), 201

