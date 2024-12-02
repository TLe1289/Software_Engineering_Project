from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class Department(models.Model):
    department_id = models.CharField(max_length=10, primary_key=True)
    building = models.CharField(max_length=50)
    office = models.CharField(max_length=50)

    def __str__(self):
        return self.department_id


class Major(models.Model):
    major_id = models.CharField(max_length=10, primary_key=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    total_hours_required = models.IntegerField()

    def __str__(self):
        return self.major_id


class Advisor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    advisor_id = models.CharField(max_length=10, primary_key=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    major = models.ForeignKey(Major, on_delete=models.CASCADE)
    building = models.CharField(max_length=50)
    office = models.CharField(max_length=50)
    phone = models.BigIntegerField()

    def __str__(self):
        return f"Advisor {self.advisor_id}"


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=10, primary_key=True)
    gender = models.CharField(max_length=1, choices=[("M", "Male"), ("F", "Female")])
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, null=True, blank=True
    )
    major = models.ForeignKey(Major, on_delete=models.SET_NULL, null=True, blank=True)
    gpa = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    credits_taken = models.IntegerField(default=0)

    def __str__(self):
        return self.student_id


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    staff_id = models.CharField(max_length=10, primary_key=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    phone = models.BigIntegerField()

    def __str__(self):
        return f"Staff {self.staff_id}"


class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    instructor_id = models.CharField(max_length=10, primary_key=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    phone = models.BigIntegerField()
    hired_semester = models.CharField(max_length=10)

    def __str__(self):
        return f"Instructor {self.instructor_id}"


class Course(models.Model):
    course_prefix = models.CharField(max_length=10)
    course_number = models.IntegerField()
    title = models.CharField(max_length=100)
    credits = models.IntegerField(default=3)

    class Meta:
        unique_together = ("course_prefix", "course_number")

    def __str__(self):
        return f"{self.course_prefix} {self.course_number}"


class InstructorCourse(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.CharField(max_length=10)
    year_taught = models.IntegerField()

    class Meta:
        unique_together = ("instructor", "course", "semester", "year_taught")

    def __str__(self):
        return f"{self.course} - {self.instructor}"


class StudentCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.CharField(max_length=10)
    year_taken = models.IntegerField()
    grade = models.CharField(max_length=2)

    class Meta:
        unique_together = ("student", "course", "semester", "year_taken")

    def __str__(self):
        return f"{self.course} - {self.student}"


class OperationLog(models.Model):
    OPERATION_CHOICES = [
        ("read", "Read"),
        ("create", "Create"),
        ("update", "Update"),
        ("delete", "Delete"),
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    operation_type = models.CharField(max_length=10, choices=OPERATION_CHOICES)
    timestamp = models.DateTimeField(default=now)
    model_name = models.CharField(max_length=100)
    data_affected = models.TextField()
    old_value = models.TextField(blank=True, null=True)
    new_value = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.timestamp} - {self.user} - {self.operation_type} - {self.model_name}"
