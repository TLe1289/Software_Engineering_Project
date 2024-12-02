from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Avg, Count, Max, Min, Sum, Case, When, FloatField
from django.shortcuts import render

from api.models import (Course, Department, InstructorCourse, Major, Student,
                        StudentCourse)


def is_staff_user(user):
    return hasattr(user, 'staff')


@user_passes_test(is_staff_user)
@login_required
def report_highest_lowest_avg_gpa(request):
    report = Major.objects.annotate(
        highest_gpa=Max('student__gpa'),
        lowest_gpa=Min('student__gpa'),
        avg_gpa=Avg('student__gpa')
    )
    return render(request, "ui/reports/report_highest_lowest_avg_gpa.html", {"report": report})


@user_passes_test(is_staff_user)
@login_required
def report_department_gpa_rank(request):
    report = Department.objects.annotate(avg_gpa=Avg('student__gpa')).order_by('-avg_gpa')
    return render(request, "ui/reports/report_department_gpa_rank.html", {"report": report})

@user_passes_test(is_staff_user)
@login_required
def report_course_enrollments(request):
    # Define grade to GPA mapping
    grade_to_points = Case(
        When(grade='A', then=4.0),
        When(grade='S', then=4.0),
        When(grade='B', then=3.0),
        When(grade='C', then=2.0),
        When(grade='D', then=1.0),
        When(grade='F', then=0.0),
        When(grade='U', then=0.0),
        When(grade='I', then=0.0),
        default=0.0,
        output_field=FloatField()
    )

    # Annotate grade points and calculate average grade
    report = StudentCourse.objects.values(
        'course__title', 'semester', 'year_taken'
    ).annotate(
        total_enrollments=Count('id'),
        avg_grade=Avg(grade_to_points)
    )

    return render(request, "ui/reports/report_course_enrollments.html", {"report": report})

@user_passes_test(is_staff_user)
@login_required
def report_instructor_students(request):
    report = InstructorCourse.objects.prefetch_related('course', 'course__studentcourse_set')
    return render(request, "ui/reports/report_instructor_students.html", {"report": report})

def report_students_by_credits(request):
    # Correct the field name for Major
    report = Student.objects.values('major__major_id').annotate(total_credits=Sum('credits_taken')).order_by('-total_credits')
    return render(request, "ui/reports/report_students_by_credits.html", {"report": report})
