from django.db import models

# 11a. Define the model: Department (name, head_of_dept, budget) in `courses/models.py``
class Department(models.Model):
    name = models.CharField(max_length=100)
    head_of_dept = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=12, decimal_places=2)

    # 12. Add __str__ methods to each model returning a human-readable string.
    def __str__(self):
        return self.name

# 11b. Define the model: Course (name, code — unique, credits, department — ForeignKey) in `courses/models.py``
class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    credits = models.PositiveIntegerField()

    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='courses')

    # 12. Add __str__ methods to each model returning a human-readable string.
    def __str__(self):
        return f"{self.code} - {self.name}"

# 11c. Define the model: Student (first_name, last_name, email — unique, department — ForeignKey, enrollment_year) in `courses/models.py``
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    enrollment_year = models.PositiveIntegerField()

    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='students')

    # 12. Add __str__ methods to each model returning a human-readable string.
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# 11d. Define the model: Enrollment (student — ForeignKey, course — ForeignKey, enrollment_date, grade — nullable CharField) in `courses/models.py``
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrollment_date = models.DateField(auto_now_add=True)
    grade = models.CharField(max_length=2, blank=True, null=True)

    # 15. Add a Meta class to the Enrollment model with unique_together = [['student','course']] to prevent duplicate enrollments.
    class Meta:
        unique_together = [["student", "course"]]

    # 12. Add __str__ methods to each model returning a human-readable string.
    def __str__(self):
        return f"{self.student} -> {self.course.code}"