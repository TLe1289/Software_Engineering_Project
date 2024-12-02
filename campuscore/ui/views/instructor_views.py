from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.db import IntegrityError, transaction
from django.shortcuts import get_object_or_404, redirect, render

from api.models import Instructor
from ui.forms import InstructorForm, InstructorUserForm
from ui.views import is_staff_user


@login_required()
@user_passes_test(is_staff_user)
def manage_instructors(request):
    if request.method == 'POST':
        form = InstructorUserForm(request.POST)
        if form.is_valid():
            try:
                # Use a transaction to ensure atomicity
                with transaction.atomic():
                    # Create the User
                    user = User.objects.create_user(
                        username=form.cleaned_data['username'],
                        email=form.cleaned_data['email'],
                        password=form.cleaned_data['password']
                    )

                    # Get the department object
                    department = form.cleaned_data['department']

                    # Create the Instructor
                    Instructor.objects.create(
                        user=user,
                        instructor_id=form.cleaned_data['instructor_id'],
                        department=department,
                        phone=form.cleaned_data['phone'],
                        hired_semester=form.cleaned_data['hired_semester']
                    )

                    messages.success(request, "Instructor added successfully.")
                    return redirect('manage_instructors')

            except IntegrityError as e:
                # Delete the user if Instructor creation fails
                if 'user' in locals():  # Check if the user object was created
                    user.delete()
                messages.error(
                    request,
                    "An instructor with this ID already exists. Please use a unique instructor ID."
                )

        else:
            messages.error(request, "Please correct the errors in the form.")

    else:
        form = InstructorUserForm()

    instructors = Instructor.objects.all()
    return render(request,
                  'ui/instructor/manage_instructors.html', {
        'form': form,
        'instructors': instructors,
    })

@login_required()
@user_passes_test(is_staff_user)
def edit_instructor(request, pk):
    instructor = get_object_or_404(Instructor, pk=pk)
    if request.method == 'POST':
        form = InstructorForm(request.POST, instance=instructor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Instructor updated successfully.')
            return redirect('manage_instructors')
    else:
        form = InstructorForm(instance=instructor)
    return render(request, 'ui/instructor/edit_instructor.html', {'form': form})

@login_required()
@user_passes_test(is_staff_user)
def delete_instructor(request, pk):
    instructor = get_object_or_404(Instructor, pk=pk)
    instructor.delete()
    messages.success(request, 'Instructor deleted successfully.')
    return redirect('manage_instructors')
