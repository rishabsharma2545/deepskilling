# 48. In courses/models.py, define Department, Course, Student, and Enrollment SQLAlchemy models 
# using db.Model as the base. Mirror the same schema used in the Django hands-on.

# 53. Add a to_dict() method to each model that returns a dictionary of its fields — 
# this is Flask's equivalent of DRF serializers.

from app import db

class Department(db.Model):
    __tablename__ = 'departments'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    code = db.Column(db.String(10), nullable=False, unique=True)
    
    courses = db.relationship('Course', back_populates='department', cascade="all, delete-orphan")
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "code": self.code
        }
    
    def __repr__(self):
        return f"<Department {self.code}>"


class Course(db.Model):
    __tablename__ = 'courses'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    code = db.Column(db.String(10), nullable=False, unique=True)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable=False)
    
    department = db.relationship('Department', back_populates='courses')
    enrollments = db.relationship('Enrollment', back_populates='course', cascade="all, delete-orphan")
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "code": self.code,
            "department_id": self.department_id
        }
    
    def __repr__(self):
        return f"<Course {self.code}>"


class Student(db.Model):
    __tablename__ = 'students'
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    
    enrollments = db.relationship('Enrollment', back_populates='student', cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email
        }
    
    def __repr__(self):
        return f"<Student {self.email}>"


class Enrollment(db.Model):
    __tablename__ = 'enrollments'
    
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    enrollment_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    student = db.relationship('Student', back_populates='enrollments')
    course = db.relationship('Course', back_populates='enrollments')
    
    def to_dict(self):
        return {
            "id": self.id,
            "student_id": self.student_id,
            "course_id": self.course_id,
            "enrollment_date": self.enrollment_date.isoformat() if self.enrollment_date else None
        }
    
    def __repr__(self):
        return f"<Enrollment Student:{self.student_id} -> Course:{self.course_id}>"