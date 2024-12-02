from django import forms
from django.contrib.auth.models import User

from api.models import Course, Department, Instructor, Major, Student


class InstructorUserForm(forms.Form):
    # User fields
    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}),
        required=True
    )

    # Instructor fields
    instructor_id = forms.CharField(
        max_length=10,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Instructor ID'})
    )
    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        empty_label="Select a Department",
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    phone = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'})
    )
    hired_semester = forms.CharField(
        max_length=10,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Hired Semester'})
    )


class StudentUserForm(forms.Form):
    # User fields
    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}),
        required=True
    )

    # Student fields
    student_id = forms.CharField(
        max_length=10,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Student ID'})
    )
    gender = forms.ChoiceField(
        choices=[("M", "Male"), ("F", "Female")],
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        empty_label="Select a Department",
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    major = forms.ModelChoiceField(
        queryset=Major.objects.all(),
        empty_label="Select a Major",
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    gpa = forms.DecimalField(
        max_digits=3,
        decimal_places=2,
        required=False,
        initial=0.0,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter GPA'})
    )
    credits_taken = forms.IntegerField(
        required=False,
        initial=0,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Credits Taken'})
    )


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"
        widgets = {
            'course_prefix': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Course Prefix'}),
            'course_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Course Number'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Course Title'}),
            'credits': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Course Credits'}),
        }


class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = "__all__"
        widgets = {
            'instructor_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Instructor ID'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
            'hired_semester': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Hired Semester'}),
        }


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        widgets = {
            'student_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Student ID'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'major': forms.Select(attrs={'class': 'form-control'}),
            'gpa': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter GPA'}),
            'credits_taken': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Credits Taken'}),
        }


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['department_id', 'building', 'office']
        widgets = {
            'department_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Department ID'}),
            'building': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Building'}),
            'office': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Office'}),
        }

class CourseEnrollmentForm(forms.Form):
    student = forms.ModelChoiceField(
        queryset=Student.objects.none(),
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    course = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    semester = forms.ChoiceField(
        choices=[
            ('Fall', 'Fall'),
            ('Spring', 'Spring'),
        ],
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    year = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 2024'})
    )
    action = forms.ChoiceField(
        choices=[('add', 'Add'), ('drop', 'Drop')],
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        advisor = kwargs.pop('advisor', None)
        super().__init__(*args, **kwargs)
        if advisor:
            # Dynamically filter students by the advisor's major
            self.fields['student'].queryset = Student.objects.filter(major=advisor.major)

from django import forms


class PredictedGPAForm(forms.Form):
    current_gpa = forms.DecimalField(
        max_digits=4,
        decimal_places=2,
        required=True,
        label="Current GPA",
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Enter current GPA"})
    )
    credits_taken = forms.IntegerField(
        required=True,
        label="Total Credits Taken",
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Enter total credits taken"})
    )
    num_courses = forms.IntegerField(
        required=False,
        label="Number of Future Courses",
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Enter number of future courses"})
    )
    credits_per_course = forms.IntegerField(
        required=False,
        label="Credits per Course",
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Enter credits per course"})
    )
    average_grade = forms.CharField(
        required=False,
        label="Expected Grade for Future Courses",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter expected grade (e.g., A, B)"})
    )


class DesiredGPAForm(forms.Form):
    current_gpa = forms.DecimalField(
        max_digits=4,
        decimal_places=2,
        required=True,
        label="Current GPA",
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Enter current GPA"})
    )
    credits_taken = forms.IntegerField(
        required=True,
        label="Total Credits Taken",
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Enter total credits taken"})
    )
    desired_gpa = forms.DecimalField(
        max_digits=4,
        decimal_places=2,
        required=True,
        label="Desired GPA",
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Enter desired GPA"})
    )
    credits_per_course = forms.IntegerField(
        required=True,
        label="Credits per Course",
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Enter credits per course"})
    )
    grade_per_course = forms.ChoiceField(
        choices=[("A", "A (4.0)"), ("B", "B (3.0)"), ("C", "C (2.0)"), ("D", "D (1.0)")],
        required=True,
        label="Grade Per Course",
        widget=forms.Select(attrs={"class": "form-control"})
    )
