CREATE DATABASE SchoolDatabase;

USE SchoolDatabase;


-- Schema for Students table
CREATE TABLE Students (
    StudentID VARCHAR(10) PRIMARY KEY,
    Gender CHAR(1) NOT NULL,
    Major VARCHAR(50),
    GPA DECIMAL(3, 2) DEFAULT 0.00 CHECK (GPA BETWEEN 0 AND 4),
    CreditsTaken INT DEFAULT 0,
    CONSTRAINT CHK_StudentID_Format CHECK (StudentID LIKE 'U%')
);

-- Schema for Departments table
CREATE TABLE Departments (
    DepartmentID VARCHAR(10),
    Building VARCHAR(50),
    Office VARCHAR(50),
    MajorOffered VARCHAR(50),
    TotalHoursReq INT,
    AdvisorID VARCHAR(10),
    AdvisorPhone INT,
    PRIMARY KEY (DepartmentID, MajorOffered, AdvisorID)
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
    InstructorCredits INT CHECK (InstructorCredits BETWEEN 1 AND 4),
    Semester VARCHAR(10),
    YearTaught INT,
    FOREIGN KEY (InstructorID) REFERENCES Instructors(InstructorID),
    PRIMARY KEY (InstructorID, CoursePrefix, CourseNumber, Semester, YearTaught)
);

-- Schema for StudentCourse table
CREATE TABLE StudentCourse (
    StudentID VARCHAR(10),
    CoursePrefix VARCHAR(10),
    CourseNumber INT,
    Semester VARCHAR(10),
    YearTaken INT,
    Grade CHAR(1) CHECK (Grade IN ('A', 'B', 'C', 'D', 'F', 'I', 'S', 'U')),
    Credits INT DEFAULT 3,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    PRIMARY KEY (StudentID, CoursePrefix, CourseNumber, Semester, YearTaken)
);

