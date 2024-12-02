from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

from api.models import Student
from ui.forms import DesiredGPAForm, PredictedGPAForm


def is_what_if_user(user):
    return hasattr(user, 'staff') or hasattr(user, 'advisor') or hasattr(user, 'student')

@user_passes_test(is_what_if_user)
@login_required
def predicted_gpa_analysis(request):
    """
    Centralized view to manage What-If analysis scenarios for students and advisors.
    """
    user = request.user
    is_advisor = hasattr(user, "advisor")
    is_student = hasattr(user, "student")
    what_if_result = None

    if request.method == "POST":
        form = PredictedGPAForm(request.POST)
        if form.is_valid():
            current_gpa = float(form.cleaned_data["current_gpa"])
            credits_taken = int(form.cleaned_data["credits_taken"])
            num_courses = form.cleaned_data.get("num_courses")
            credits_per_course = form.cleaned_data.get("credits_per_course")
            average_grade = form.cleaned_data.get("average_grade")

            # Perform What-If Analysis
            if num_courses and credits_per_course and average_grade:
                total_points = current_gpa * credits_taken
                future_points = num_courses * credits_per_course * grade_to_points(average_grade)
                new_gpa = (total_points + future_points) / (credits_taken + num_courses * credits_per_course)
                what_if_result = f"New GPA after {num_courses} courses: {new_gpa:.2f}"
    else:
        form = PredictedGPAForm()

    context = {
        "form": form,
        "what_if_result": what_if_result,
        "is_advisor": is_advisor,
        "is_student": is_student,
    }
    return render(request, "ui/whatif/predicted_gpa_analysis.html", context)

@user_passes_test(is_what_if_user)
@login_required
def desired_gpa_analysis(request):
    result = None

    if request.method == "POST":
        form = DesiredGPAForm(request.POST)
        if form.is_valid():
            current_gpa = float(form.cleaned_data["current_gpa"])
            credits_taken = int(form.cleaned_data["credits_taken"])
            desired_gpa = float(form.cleaned_data["desired_gpa"])
            credits_per_course = int(form.cleaned_data["credits_per_course"])
            grade_per_course = form.cleaned_data["grade_per_course"]

            # Convert grade to points
            grade_points = grade_to_points(grade_per_course)

            # Calculate number of courses needed
            total_points_required = desired_gpa * (credits_taken + credits_per_course)
            current_points = current_gpa * credits_taken
            points_needed = total_points_required - current_points

            if points_needed <= 0:
                result = "You have already achieved the desired GPA!"
            else:
                num_courses_required = points_needed / (credits_per_course * grade_points)
                result = f"You need to take approximately {int(num_courses_required)} courses with grade '{grade_per_course}' to achieve a GPA of {desired_gpa}."

    else:
        form = DesiredGPAForm()

    return render(request, "ui/whatif/desired_gpa_analysis.html", {"form": form, "result": result})


def grade_to_points(grade):
    """Convert grade to GPA points."""
    grades = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}
    return grades.get(grade.upper(), 0.0)



def calculate_scenario1(request):
    if request.method == "POST":
        current_gpa = float(request.POST["currentGPA"])
        num_courses_taken = int(request.POST["numCoursesTaken"])
        num_courses = int(request.POST["numCourses"])
        credits_per_course = int(request.POST["creditsPerCourse"])
        average_grade = request.POST["averageGrade"]

        # Grade-to-GPA conversion
        grade_to_numeric = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}
        grade_value = grade_to_numeric.get(average_grade.upper(), 0.0)

        # Calculate new GPA
        new_quality_points = num_courses * credits_per_course * grade_value
        total_credits = (num_courses_taken + num_courses) * credits_per_course
        new_gpa = (current_gpa * (num_courses_taken * credits_per_course) + new_quality_points) / total_credits

        student = Student.objects.get(student_id="U123456")  # Replace with logic for logged-in student
        return render(
            request,
            "student_dashboard.html",
            {
                "student": student,
                "result": f"New GPA: {round(new_gpa, 2)}",
                "courses_taken": num_courses_taken,
                "current_gpa": current_gpa,
            },
        )


def calculate_scenario2(request):
    if request.method == "POST":
        current_gpa = float(request.POST["currentGPA"])
        num_courses_taken = int(request.POST["numCoursesTaken"])
        desired_gpa = float(request.POST["desiredGPA"])
        credits_per_course = int(request.POST["creditsPerCourse"])
        average_grade = request.POST["averageGrade"]

        # Grade-to-GPA conversion
        grade_to_numeric = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}
        grade_value = grade_to_numeric.get(average_grade.upper(), 0.0)

        # Calculate additional courses needed
        current_quality_points = current_gpa * num_courses_taken * credits_per_course
        desired_quality_points = desired_gpa * (num_courses_taken + 1) * credits_per_course
        additional_quality_points_needed = desired_quality_points - current_quality_points
        num_courses_required = int(-(-additional_quality_points_needed // (credits_per_course * grade_value)))  # Ceiling division

        student = Student.objects.get(student_id="U123456")  # Replace with logic for logged-in student
        return render(
            request,
            "student_dashboard.html",
            {
                "student": student,
                "result": f"Courses Required: {num_courses_required}",
                "courses_taken": num_courses_taken,
                "current_gpa": current_gpa,
            },
        )
