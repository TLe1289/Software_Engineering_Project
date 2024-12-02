
# from django.contrib import admin
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from . import views

urlpatterns = [

    path('landing/', views.landing_page, name='landing_page'),

    # Manage Courses
    path("staff/courses/", views.manage_courses, name="manage_courses"),
    path("staff/courses/<int:pk>/edit/", views.edit_course, name="edit_course"),
    path(
        "staff/courses/<int:pk>/delete/", views.delete_course,
        name="delete_course"),
    # Manage Instructors
    path('instructors/', views.manage_instructors, name='manage_instructors'),
    path('instructors/edit/<str:pk>/', views.edit_instructor, name='edit_instructor'),
    path(
        'instructors/delete/<str:pk>/', views.delete_instructor,
        name='delete_instructor'),

    # Manage Students
    path('students/', views.manage_students, name='manage_students'),
    path('students/edit/<str:pk>/', views.edit_student, name='edit_student'),
    path('students/delete/<str:pk>/', views.delete_student, name='delete_student'),

    # Manage Departments
    path('departments/', views.manage_departments, name='manage_departments'),
    path('departments/edit/<str:pk>/', views.edit_department, name='edit_department'),
    path(
        'departments/delete/<str:pk>/', views.delete_department,
        name='delete_department'),

    # Manage Whatifs
    path('whatif/predicted/', views.predicted_gpa_analysis, name='predicted_gpa_analysis'),
    path('whatif/desired/', views.desired_gpa_analysis, name='desired_gpa_analysis'),

    # Reports
    path("reporting/", views.report_dashboard, name="report_dashboard"),
    path(
        "report/highest-lowest-avg-gpa/", views.report_highest_lowest_avg_gpa,
        name="report_highest_lowest_avg_gpa"),
    path(
        "report/department-gpa-rank/", views.report_department_gpa_rank,
        name="report_department_gpa_rank"),
    path(
        "report/course-enrollments/", views.report_course_enrollments,
        name="report_course_enrollments"),
    path(
        "report/instructor-students/", views.report_instructor_students,
        name="report_instructor_students"),
    path(
        "report/students-by-credits/", views.report_students_by_credits,
        name="report_students_by_credits"),

    # Rest of application URLs
    path("", views.index),

    # Custom Registration View
    path('register/', views.register_view, name='register'),

    # Login and Logout using built-in views
    path('login/', auth_views.LoginView.as_view(template_name='ui/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Password Reset Flows using built-in views
    path('forgot-password/', auth_views.PasswordResetView.as_view(
        template_name='ui/forgot_password.html',
        email_template_name='ui/password_reset_email.html',
        success_url='/forgot-password-done/'
    ), name='forgot_password'),
    path('forgot-password-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='ui/forgot_password_done.html'
    ), name='password_reset_done'),
    path('reset-password/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='ui/reset_password.html',
        success_url='/reset-password-complete/'
    ), name='password_reset_confirm'),
    path('reset-password-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='ui/reset_password_complete.html'
    ), name='password_reset_complete'),
]
