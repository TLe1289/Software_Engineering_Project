from django.contrib import admin

from .models import (Advisor, Course, Department, Instructor, InstructorCourse,
                     Major, OperationLog, Staff, Student, StudentCourse)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("department_id", "building", "office")
    search_fields = ("department_id", "building")


@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    list_display = ("major_id", "department", "total_hours_required")
    search_fields = ("major_id", "department__department_id")
    list_filter = ("department",)


@admin.register(Advisor)
class AdvisorAdmin(admin.ModelAdmin):
    list_display = (
        "advisor_id",
        "user",
        "department",
        "major",
        "building",
        "office",
        "phone",
    )
    search_fields = (
        "advisor_id",
        "user__username",
        "department__department_id",
        "major__major_id",
    )
    list_filter = ("department", "major")


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "student_id",
        "user",
        "gender",
        "department",
        "major",
        "gpa",
        "credits_taken",
    )
    search_fields = (
        "student_id",
        "user__username",
        "major__major_id",
        "department__department_id",
    )
    list_filter = ("gender", "department", "major")
    list_editable = ("gpa", "credits_taken")


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ("staff_id", "user", "department", "phone")
    search_fields = ("staff_id", "user__username", "department__department_id")
    list_filter = ("department",)


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ("instructor_id", "user", "department", "phone", "hired_semester")
    search_fields = ("instructor_id", "user__username", "department__department_id")
    list_filter = ("department", "hired_semester")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("course_prefix", "course_number", "title", "credits")
    search_fields = ("course_prefix", "course_number", "title")
    list_filter = ("credits",)


@admin.register(InstructorCourse)
class InstructorCourseAdmin(admin.ModelAdmin):
    list_display = ("instructor", "course", "semester", "year_taught")
    search_fields = (
        "instructor__instructor_id",
        "course__title",
        "semester",
        "year_taught",
    )
    list_filter = ("semester", "year_taught")


@admin.register(StudentCourse)
class StudentCourseAdmin(admin.ModelAdmin):
    list_display = ("student", "course", "semester", "year_taken", "grade")
    search_fields = ("student__student_id", "course__title", "semester", "year_taken")
    list_filter = ("semester", "year_taken", "grade")


@admin.register(OperationLog)
class OperationLogAdmin(admin.ModelAdmin):
    list_display = ("timestamp", "user", "operation_type", "model_name")
    list_filter = ("operation_type", "model_name", "timestamp")
    search_fields = ("user__username", "model_name", "data_affected")
