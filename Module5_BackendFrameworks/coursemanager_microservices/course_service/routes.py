from flask import Blueprint, jsonify, request
from extensions import db
from models import Course, Department

course_bp = Blueprint("courses", __name__, url_prefix="/api/courses")

def make_response_json(data, status_code=200):
    return jsonify({"status": "success", "data": data}), status_code


# GET /api/courses
@course_bp.route("/", methods=["GET"])
def get_courses():
    courses = Course.query.all()
    return make_response_json(
        [course.to_dict() for course in courses]
    )


# GET /api/courses/<id>
@course_bp.route("/<int:course_id>", methods=["GET"])
def get_course(course_id):
    course = Course.query.get_or_404(course_id)
    return make_response_json(course.to_dict())


# POST /api/courses
@course_bp.route("/", methods=["POST"])
def create_course():
    data = request.get_json()

    new_course = Course(title=data["title"], code=data["code"], department_id=data["department_id"])

    db.session.add(new_course)
    db.session.commit()

    return make_response_json(new_course.to_dict(), 201)


# PUT /api/courses/<id>
@course_bp.route("/<int:course_id>", methods=["PUT"])
def update_course(course_id):
    course = Course.query.get_or_404(course_id)

    data = request.get_json()

    course.title = data.get("title", course.title)
    course.code = data.get("code", course.code)
    course.department_id = data.get("department_id", course.department_id)

    db.session.commit()

    return make_response_json(course.to_dict())


# DELETE /api/courses/<id>
@course_bp.route("/<int:course_id>", methods=["DELETE"])
def delete_course(course_id):
    course = Course.query.get_or_404(course_id)

    db.session.delete(course)
    db.session.commit()

    return jsonify({"status": "success", "message": f"Course {course_id} deleted successfully."}), 200


# GET /api/departments
@course_bp.route("/departments", methods=["GET"])
def get_departments():
    departments = Department.query.all()

    return make_response_json(
        [department.to_dict() for department in departments]
    )


# GET /api/departments/<id>
@course_bp.route("/departments/<int:department_id>", methods=["GET"])
def get_department(department_id):
    department = Department.query.get_or_404(department_id)

    return make_response_json(department.to_dict()    )


# POST /api/departments
@course_bp.route("/departments", methods=["POST"])
def create_department():
    data = request.get_json()

    department = Department(name=data["name"], code=data["code"])

    db.session.add(department)
    db.session.commit()

    return make_response_json(department.to_dict(), 201)


# PUT /api/departments/<id>
@course_bp.route("/departments/<int:department_id>", methods=["PUT"])
def update_department(department_id):

    department = Department.query.get_or_404(department_id)

    data = request.get_json()

    department.name = data.get("name", department.name)

    department.code = data.get("code", department.code)

    db.session.commit()

    return make_response_json(department.to_dict())


# DELETE /api/departments/<id>
@course_bp.route("/departments/<int:department_id>", methods=["DELETE"])
def delete_department(department_id):

    department = Department.query.get_or_404(department_id)

    db.session.delete(department)
    db.session.commit()

    return jsonify({"status": "success", "message": f"Department {department_id} deleted successfully."}), 200