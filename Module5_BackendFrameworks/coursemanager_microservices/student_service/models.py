from extensions import db

class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)

    enrollments = db.relationship("Enrollment", back_populates="student", cascade="all, delete-orphan")

    def to_dict(self):
        return {"id": self.id, "first_name": self.first_name, "last_name": self.last_name, "email": self.email}

    def __repr__(self):
        return f"<Student {self.email}>"


class Enrollment(db.Model):
    __tablename__ = "enrollments"

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("students.id"), nullable=False)
    course_id = db.Column(db.Integer, nullable=False)
    enrollment_date = db.Column(db.DateTime, default=db.func.current_timestamp())

    student = db.relationship("Student", back_populates="enrollments")

    def to_dict(self):
        return {"id": self.id, "student_id": self.student_id, "course_id": self.course_id, "enrollment_date": (self.enrollment_date.isoformat() if self.enrollment_date else None)}

    def __repr__(self):
        return (f"<Enrollment Student:{self.student_id}" f"Course:{self.course_id}>")