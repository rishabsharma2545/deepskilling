from extensions import db

class Department(db.Model):
    __tablename__ = "departments"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    code = db.Column(db.String(10), nullable=False, unique=True)

    courses = db.relationship("Course", back_populates="department", cascade="all, delete-orphan")

    def to_dict(self):
        return {"id": self.id, "name": self.name, "code": self.code}

    def __repr__(self):
        return f"<Department {self.code}>"
    

class Course(db.Model):
    __tablename__ = "courses"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    code = db.Column(db.String(10), nullable=False, unique=True)

    department_id = db.Column(db.Integer, db.ForeignKey("departments.id"), nullable=False)

    department = db.relationship("Department", back_populates="courses")

    def to_dict(self):
        return {"id": self.id, "title": self.title, "code": self.code, "department_id": self.department_id}

    def __repr__(self):
        return f"<Course {self.code}>"
