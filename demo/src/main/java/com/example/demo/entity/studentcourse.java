package com.example.demo.entity;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;


@Entity
@Table(name = "studentcourse")
public class studentcourse {

    @Id
    private String StudentID;
    private String CoursePrefix;
    private int CourseNumber;
    private String Semester;
    private int YearTaken;
    private char Grade;

    // Getters and Setters

    public String getStudentID() {
        return StudentID;
    }

    public void setStudentID(String StudentID) {
        this.StudentID = StudentID;
    }

    public String getCoursePrefix() {
        return CoursePrefix;
    }

    public void setCoursePrefix(String CoursePrefix) {
        this.CoursePrefix = CoursePrefix;
    }

    public int getCourseNumber() {
        return CourseNumber;
    }

    public void setCourseNumber(int CourseNumber) {
        this.CourseNumber = CourseNumber;
    }

    public String getSemester() {
        return Semester;
    }

    public void setSemester(String Semester) {
        this.Semester = Semester;
    }

    public int getYearTaken() {
        return YearTaken;
    }

    public void setYearTaken(int YearTaken) {
        this.YearTaken = YearTaken;
    }

    public char getGrade() {
        return Grade;
    }

    public void setGrade(char Grade) {
        this.Grade = Grade;
    }
}
