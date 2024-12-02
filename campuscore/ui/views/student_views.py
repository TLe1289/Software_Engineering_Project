from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.db import IntegrityError, transaction
from django.shortcuts import get_object_or_404, redirect, render

from api.models import Student
from ui.forms import StudentForm, StudentUserForm
from ui.views import is_staff_user


@login_required()
@user_passes_test(is_staff_user)
def manage_students(request):
    if request.method == 'POST':
        form = StudentUserForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    # Create the User
                    user = User.objects.create_user(
                        username=form.cleaned_data['username'],
                        email=form.cleaned_data['email'],
                        password=form.cleaned_data['password']
                    )

                    # Get the department and major objects
                    department = form.cleaned_data['department']
                    major = form.cleaned_data['major']

                    # Create the Student
                    Student.objects.create(
                        user=user,
                        student_id=form.cleaned_data['student_id'],
                        gender=form.cleaned_data['gender'],
                        department=department,
                        major=major,
                        gpa=form.cleaned_data['gpa'],
                        credits_taken=form.cleaned_data['credits_taken']
                    )

                    messages.success(request, "Student added successfully.")
                    return redirect('manage_students')

            except IntegrityError as e:
                # Delete the user if Student creation fails
                if 'user' in locals():
                    user.delete()
                messages.error(
                    request,
                    "A student with this ID already exists. Please use a unique student ID."
                )

        else:
            messages.error(request, "Please correct the errors in the form.")

    else:
        form = StudentUserForm()

    students = Student.objects.all()
    return render(request, 'ui/student/manage_students.html', {
        'form': form,
        'students': students,
    })

@login_required()
@user_passes_test(is_staff_user)
def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student updated successfully.')
            return redirect('manage_students')
    else:
        form = StudentForm(instance=student)
    return render(request, 'ui/student/edit_student.html', {'form': form})

@login_required()
@user_passes_test(is_staff_user)
def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    messages.success(request, 'Student deleted successfully.')
    return redirect('manage_students')
