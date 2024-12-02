from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.db import IntegrityError, transaction
from django.db.models import Avg, F
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from api.models import (Advisor, Course, Department, Instructor, Staff,
                        Student, StudentCourse)
from ui.forms import (CourseForm, DepartmentForm, InstructorForm,
                      InstructorUserForm, StudentForm, StudentUserForm)

from . import is_staff_user


@login_required()
@user_passes_test(is_staff_user)
def manage_departments(request):
    departments = Department.objects.all()
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("manage_departments")
    else:
        form = DepartmentForm()
    return render(request,
                  "ui/department/manage_departments.html", {"departments": departments, "form": form})


@login_required()
@user_passes_test(is_staff_user)
def edit_department(request, pk):
    """View to edit an existing department."""
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            messages.success(request, "Department updated successfully.")
            return redirect('manage_departments')
        else:
            messages.error(request, "Please correct the errors in the form.")
    else:
        form = DepartmentForm(instance=department)

    return render(request, 'ui/department/edit_department.html', {
        'form': form,
        'department': department,
    })

@login_required()
@user_passes_test(is_staff_user)
def delete_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    department.delete()
    messages.success(request, 'Student deleted successfully.')
    return redirect('manage_departments')

