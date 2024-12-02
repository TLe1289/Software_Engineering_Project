from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views
from .views import (DepartmentViewSet, InstructorCourseViewSet,
                    InstructorViewSet, StaffViewSet, StudentCourseViewSet,
                    StudentViewSet)

router = DefaultRouter()
router.register(r"students", StudentViewSet)
router.register(r"departments", DepartmentViewSet)
router.register(r"staffs", StaffViewSet)
router.register(r"instructors", InstructorViewSet)
router.register(r"instructor-courses", InstructorCourseViewSet)
router.register(r"student-courses", StudentCourseViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("what-if/scenario1/", views.calculate_scenario1, name="calculate_scenario1"),
    path("what-if/scenario2/", views.calculate_scenario2, name="calculate_scenario2"),
]
