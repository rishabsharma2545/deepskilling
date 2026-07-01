from flask import jsonify, request
from app import db
from courses import courses_bp
from courses.models import Course, Student, Enrollment

# 44. Helper function to return a consistent JSON envelope
def make_response_json(data, status_code=200, status_str='success'):
    response = {'status': status_str, 'data': data}
    return jsonify(response), status_code


# 52 & 54. GET all courses & POST a new course
@courses_bp.route('/', methods=['GET'])
def get_courses():
    # Query database for all courses
    courses = db.session.execute(db.select(Course)).scalars().all()
    # Serialize results to a list of dicts using model's to_dict() method
    serialized_courses = [course.to_dict() for course in courses]
    return make_response_json(serialized_courses, 200)


@courses_bp.route('/', methods=['POST'])
def create_course():
    data = request.get_json() or {}

    # Validate that required fields are present (matching SQLAlchemy model attributes)
    required_fields = ['title', 'code', 'department_id']
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        return make_response_json(
            data={"error": f"Missing required fields: {missing_fields}"},
            status_code=400, 
            status_str='fail'
        )

    # Create new Course object using DB attributes
    new_course = Course(
        title=data['title'],
        code=data['code'],
        department_id=data['department_id']
    )
    
    db.session.add(new_course)
    db.session.commit()

    return make_response_json(new_course.to_dict(), 201)      


# 55. GET, PUT, and DELETE routes using Course.query.get_or_404(id) equivalent 
# (Flask-SQLAlchemy 3.x+ modern alternative: db.one_or_404)
@courses_bp.route('/<int:course_id>/', methods=['GET'])
def get_course(course_id):
    # Automatically raises a 404 error if the course isn't found
    course = db.one_or_404(db.select(Course).filter_by(id=course_id))
    return make_response_json(course.to_dict(), 200)


@courses_bp.route('/<int:course_id>/', methods=['PUT'])
def update_course(course_id):
    course = db.one_or_404(db.select(Course).filter_by(id=course_id))
    data = request.get_json() or {}
    
    # Update properties dynamically based on input or retain current values
    course.title = data.get('title', course.title)
    course.code = data.get('code', course.code)
    course.department_id = data.get('department_id', course.department_id)
    
    db.session.commit()
    return make_response_json(course.to_dict(), 200)


@courses_bp.route('/<int:course_id>/', methods=['DELETE'])
def delete_course(course_id):
    course = db.one_or_404(db.select(Course).filter_by(id=course_id))
    
    db.session.delete(course)
    db.session.commit()
    return make_response_json({"message": f"Course {course_id} deleted successfully"}, 200)


# 56. JOIN query route to return all students enrolled in a specified course
@courses_bp.route('/<int:course_id>/students/', methods=['GET'])
def get_course_students(course_id):
    # First verify the course actually exists
    db.one_or_404(db.select(Course).filter_by(id=course_id))
    
    # Explicit JOIN query: Student -> Enrollment filtered by course_id
    stmt = (
        db.select(Student)
        .join(Enrollment, Student.id == Enrollment.student_id)
        .where(Enrollment.course_id == course_id)
    )
    students = db.session.execute(stmt).scalars().all()
    
    serialized_students = [student.to_dict() for student in students]
    return make_response_json(serialized_students, 200)