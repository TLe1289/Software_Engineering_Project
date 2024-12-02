from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, redirect, render

from api.models import Course
from ui.forms import CourseForm
from ui.views import is_staff_user


@login_required()
@user_passes_test(is_staff_user)
def manage_courses(request):
    courses = Course.objects.all()
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("manage_courses")
    else:
        form = CourseForm()
    return render(request, "ui/course/manage_courses.html", {"courses": courses, "form": form})

@user_passes_test(is_staff_user)
def edit_course(request, pk):
    course = get_object_or_404(Course, id=pk)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect("manage_courses")
    else:
        form = CourseForm(instance=course)
    return render(request, "ui/course/edit_course.html", {"form": form, "course": course})

@user_passes_test(is_staff_user)
def delete_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    course.delete()
    messages.success(request, 'Student deleted successfully.')
    return redirect('manage_courses')

