from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import redirect, render

from api.models import (Course, InstructorCourse, Major, OperationLog, Student,
                        StudentCourse)
from ui.forms import CourseEnrollmentForm


def is_staff_user(user):
    return hasattr(user, 'staff')

@login_required
def index(request):
    return render(request, "ui/index.html")


# Custom Registration View
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Account created successfully. Please log in.')
            return redirect('login')
    return render(request, 'ui/register.html')


@login_required
def landing_page(request):
    """
    Renders a landing page based on the user type.
    The user_type is determined by checking the related model of the logged-in user.
    """
    user = request.user

    OperationLog.objects.create(
        user=user,
        operation_type='read',
        model_name='LandingPage',
        data_affected='Accessed landing page'
    )

    # Determine user type and associated data
    if hasattr(user, 'staff'):
        return staff_dashboard(request)
    elif hasattr(user, 'advisor'):
        return advisor_dashboard(request)
    elif hasattr(user, 'student'):
        return student_dashboard(request)
    elif hasattr(user, 'instructor'):
        return instructor_dashboard(request)
    else:
        # Redirect to a default page or show an error message for unrecognized user types
        return redirect('login')


@login_required
def staff_dashboard(request):
    """View for the staff dashboard."""
    OperationLog.objects.create(
        user=request.user,
        operation_type='read',
        model_name='Staff',
        data_affected=f"Accessed staff dashboard for staff ID {request.user.staff.staff_id}"
    )

    return render(request,  'ui/staff_landing.html', {})

@login_required
def advisor_dashboard(request):
    """Renders the advisor dashboard and handles course enrollment/withdrawal."""
    advisor = request.user.advisor
    students = Student.objects.filter(major=advisor.major)

    if request.method == 'POST':
        form = CourseEnrollmentForm(request.POST, advisor=advisor)
        if form.is_valid():
            student = form.cleaned_data['student']
            print(student)
            course = form.cleaned_data['course']
            print(course)
            action = form.cleaned_data['action']
            print(action)

            try:
                if action == 'add':
                    # Enroll student in the course
                    enrollment = StudentCourse.objects.create(
                        student=student,
                        course=course,
                        semester=form.cleaned_data['semester'],
                        year_taken=form.cleaned_data['year']
                    )
                    messages.success(request, f"Student {student.student_id} successfully enrolled in {course}.")
                    OperationLog.objects.create(
                        user=request.user,
                        operation_type='create',
                        model_name='StudentCourse',
                        data_affected=f"Student {student.student_id} enrolled in {course}",
                        new_value={
                            'student_id': student.student_id,
                            'course_id': course.id,
                            'semester': enrollment.semester,
                            'year': enrollment.year_taken,
                        }
                    )
                elif action == 'drop':
                    # Drop student from the course
                    enrollment = StudentCourse.objects.get(
                        student=student,
                        course=course,
                        semester=form.cleaned_data['semester'],
                        year_taken=form.cleaned_data['year']
                    )
                    enrollment.delete()
                    messages.success(request, f"Student {student.student_id} successfully dropped from {course}.")
                    OperationLog.objects.create(
                        user=request.user,
                        operation_type='delete',
                        model_name='StudentCourse',
                        data_affected=f"Student {student.student_id} dropped from {course}",
                        old_value={
                            'student_id': student.student_id,
                            'course_id' : course.id,
                            'semester'  : enrollment.semester,
                            'year'      : enrollment.year_taken,
                        }
                    )
            except IntegrityError as e:
                messages.error(request, f"Error processing the request: {e}")
            except StudentCourse.DoesNotExist:
                messages.error(request, f"Student {student.student_id} is not enrolled in {course}.")

            return redirect('landing_page')
    else:
        form = CourseEnrollmentForm(advisor=advisor)

    OperationLog.objects.create(
        user=request.user,
        operation_type='read',
        model_name='AdvisorDashboard',
        data_affected=f"Accessed advisor dashboard for advisor ID {advisor.advisor_id}"
    )

    return render(request, 'ui/advisor_landing.html', {
        'advisor': advisor,
        'students': students,
        'form': form,
    })

@login_required
def student_dashboard(request):
    """View for the student dashboard."""
    student = request.user.student
    enrolled_courses = StudentCourse.objects.filter(student=student)

    OperationLog.objects.create(
        user=request.user,
        operation_type='read',
        model_name='StudentDashboard',
        data_affected=f"Accessed student dashboard for student ID {student.student_id}"
    )

    return render(request, 'ui/student_landing.html', {
        'user': request.user,
        'student': student,
        'enrolled_courses': enrolled_courses,
    })
    return render(request, template, context)

@login_required
def instructor_dashboard(request):
    """View for the instructor dashboard."""
    instructor = request.user.instructor
    assigned_courses = InstructorCourse.objects.filter(instructor=instructor)

    OperationLog.objects.create(
        user=request.user,
        operation_type='read',
        model_name='InstructorDashboard',
        data_affected=f"Accessed instructor dashboard for instructor ID {instructor.instructor_id}"
    )

    return render(request, 'ui/instructor_landing.html', {
        'user': request.user,
        'instructor': instructor,
        'assigned_courses': assigned_courses,
    })

@login_required
def report_dashboard(request):
    """
    Main reporting page with links to individual reports.
    """
    return render(request, "ui/report_landing.html")

from .course_views import *
from .department_views import *
from .instructor_views import *
from .report_views import *
from .student_views import *
from .whatif_views import *
