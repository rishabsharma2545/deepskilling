from flask import Blueprint, jsonify, request

from extensions import db
from models import Student, Enrollment
import requests
from requests.exceptions import ConnectionError

student_bp = Blueprint("students", __name__, url_prefix="/api/students")


def make_response_json(data, status_code=200):
    return jsonify({"status": "success", "data": data}), status_code


# GET /api/students
@student_bp.route("/", methods=["GET"])
def get_students():
    students = Student.query.all()

    return make_response_json(
        [student.to_dict() for student in students]
    )


# GET /api/students/<id>
@student_bp.route("/<int:student_id>", methods=["GET"])
def get_student(student_id):
    student = Student.query.get_or_404(student_id)

    return make_response_json(student.to_dict())


# POST /api/students
@student_bp.route("/", methods=["POST"])
def create_student():
    data = request.get_json()

    student = Student(first_name=data["first_name"], last_name=data["last_name"], email=data["email"])

    db.session.add(student)
    db.session.commit()

    return make_response_json(student.to_dict(), 201)


# PUT /api/students/<id>
@student_bp.route("/<int:student_id>", methods=["PUT"])
def update_student(student_id):

    student = Student.query.get_or_404(student_id)
    data = request.get_json()

    student.first_name = data.get("first_name", student.first_name)
    student.last_name = data.get("last_name", student.last_name)
    student.email = data.get("email", student.email)

    db.session.commit()

    return make_response_json(student.to_dict())


# DELETE /api/students/<id>
@student_bp.route("/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):

    student = Student.query.get_or_404(student_id)

    db.session.delete(student)
    db.session.commit()

    return jsonify({"status": "success", "message": f"Student {student_id} deleted successfully."}), 200


# POST /api/students/<id>/enroll
import requests
from requests.exceptions import ConnectionError


@student_bp.route("/<int:student_id>/enroll", methods=["POST"])
def enroll_student(student_id):

    student = Student.query.get_or_404(student_id)

    data = request.get_json()
    course_id = data["course_id"]

    try:
        response = requests.get(f"http://127.0.0.1:5001/api/courses/{course_id}")

    except ConnectionError:
        return jsonify({"status": "error", "message": "Course Service is currently unavailable. Please try again later."}), 503

    if response.status_code == 404:
        return jsonify({"status": "error", "message": f"Course {course_id} does not exist."}), 404

    enrollment = Enrollment(student_id=student.id, course_id=course_id)

    db.session.add(enrollment)
    db.session.commit()

    return make_response_json(enrollment.to_dict(),201)