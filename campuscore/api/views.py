import json
import math

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets

from .models import (Department, Instructor, InstructorCourse, Staff, Student,
                     StudentCourse)
from .serializers import (DepartmentSerializer, InstructorCourseSerializer,
                          InstructorSerializer, StaffSerializer,
                          StudentCourseSerializer, StudentSerializer)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


class InstructorViewSet(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer


class InstructorCourseViewSet(viewsets.ModelViewSet):
    queryset = InstructorCourse.objects.all()
    serializer_class = InstructorCourseSerializer


class StudentCourseViewSet(viewsets.ModelViewSet):
    queryset = StudentCourse.objects.all()
    serializer_class = StudentCourseSerializer


@csrf_exempt
def calculate_scenario1(request):
    if request.method == "POST":
        try:
            # Parse and validate input data
            payload = json.loads(request.body)
            current_gpa = float(payload.get("currentGPA", 0))
            num_courses_taken = int(payload.get("numCoursesTaken", 0))
            num_courses = int(payload.get("numCourses", 0))
            credits_per_course = int(payload.get("creditsPerCourse", 0))
            average_grade = payload.get("averageGrade")

            # Validate inputs
            if not all(
                [
                    current_gpa,
                    num_courses_taken,
                    num_courses,
                    credits_per_course,
                    average_grade,
                ]
            ):
                return JsonResponse(
                    {"error": "Missing or invalid input fields."}, status=400
                )

            # Convert grade to numeric value
            grade_value = grade_to_numeric(average_grade)

            # Calculate total quality points and GPA
            new_quality_points = num_courses * credits_per_course * grade_value
            total_credits = (num_courses_taken + num_courses) * credits_per_course
            new_gpa = (
                current_gpa * (num_courses_taken * credits_per_course)
                + new_quality_points
            ) / total_credits

            # Response
            return JsonResponse({"newGPA": new_gpa}, status=200)

        except (ValueError, KeyError):
            return JsonResponse(
                {"error": "Invalid number format. Please check your inputs."},
                status=400,
            )
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Only POST method is allowed."}, status=405)


@csrf_exempt
def calculate_scenario2(request):
    if request.method == "POST":
        try:
            # Parse and validate input data
            payload = json.loads(request.body)
            current_gpa = float(payload.get("currentGPA", 0))
            desired_gpa = float(payload.get("desiredGPA", 0))
            num_courses_taken = int(payload.get("numCoursesTaken", 0))
            credits_per_course = int(payload.get("creditsPerCourse", 0))
            average_grade = payload.get("averageGrade")

            # Validate inputs
            if not all(
                [
                    current_gpa,
                    desired_gpa,
                    num_courses_taken,
                    credits_per_course,
                    average_grade,
                ]
            ):
                return JsonResponse(
                    {"error": "Missing or invalid input fields."}, status=400
                )

            # Convert grade to numeric value
            grade_value = grade_to_numeric(average_grade)

            # Calculate additional quality points and courses required
            current_quality_points = (
                current_gpa * num_courses_taken * credits_per_course
            )
            desired_quality_points = (
                desired_gpa * (num_courses_taken + 1) * credits_per_course
            )
            additional_quality_points_needed = (
                desired_quality_points - current_quality_points
            )
            num_courses_required = math.ceil(
                additional_quality_points_needed / (credits_per_course * grade_value)
            )

            # Response
            return JsonResponse(
                {"numCoursesRequired": num_courses_required}, status=200
            )

        except (ValueError, KeyError):
            return JsonResponse(
                {"error": "Invalid number format. Please check your inputs."},
                status=400,
            )
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Only POST method is allowed."}, status=405)


# Helper function to convert grades to numeric values
def grade_to_numeric(grade):
    grade_map = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}
    grade_value = grade_map.get(grade.upper())
    if grade_value is None:
        raise ValueError(f"Invalid grade: {grade}")
    return grade_value
