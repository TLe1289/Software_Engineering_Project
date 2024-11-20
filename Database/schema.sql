CREATE DATABASE SchoolDatabase;

USE SchoolDatabase;


-- Schema for Students table
CREATE TABLE Students (
    StudentID VARCHAR(10) PRIMARY KEY,
    Gender CHAR(1) NOT NULL,
    Major VARCHAR(50)
);

-- Schema for Departments table
CREATE TABLE Departments (
    DepartmentID VARCHAR(10),
    Building VARCHAR(50),
    Office VARCHAR(50),
    MajorOffered VARCHAR(50),
    TotalHoursReq INT,
    AdvisorID VARCHAR(10),
    AdvisorPhone INT
);

-- Schema for Staffs table
CREATE TABLE Staffs (
    StaffID VARCHAR(10) PRIMARY KEY,
    DepartmentID VARCHAR(10),
    Phone INT
);

-- Schema for Instructors table
CREATE TABLE Instructors (
    InstructorID VARCHAR(10) PRIMARY KEY,
    InstructorPhone INT NOT NULL,
    DepartmentID VARCHAR(10),
    HiredSemester VARCHAR(10)
);

-- Schema for InstructorCourse table
CREATE TABLE InstructorCourse (
    InstructorID VARCHAR(10),
    CoursePrefix VARCHAR(10),
    CourseNumber INT,
    Credits INT,
    Semester VARCHAR(10),
    YearTaught INT,
    FOREIGN KEY (InstructorID) REFERENCES Instructors(InstructorID)
);

-- Schema for StudentCourse table
CREATE TABLE StudentCourse (
    StudentID VARCHAR(10),
    CoursePrefix VARCHAR(10),
    CourseNumber INT,
    Semester VARCHAR(10),
    YearTaken INT,
    Grade CHAR(1),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
);

