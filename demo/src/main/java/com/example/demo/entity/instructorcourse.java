package com.example.demo.entity;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;


@Entity
@Table(name = "instructorcourse")
public class instructorcourse {

    @Id
    private String InstructorID;
    private String CoursePrefix;
    private int CourseNumber;
    private int Credits;
    private String Semester;
    private int YearTaught;

    // Getters and Setters

    public String getInstructorID() {
        return InstructorID;
    }

    public void setInstructorID(String InstructorID) {
        this.InstructorID = InstructorID;
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

    public int getCredits() {
        return Credits;
    }

    public void setCredits(int Credits) {
        this.Credits = Credits;
    }

    public String getSemester() {
        return Semester;
    }

    public void setSemester(String Semester) {
        this.Semester = Semester;
    }

    public int getYearTaught() {
        return YearTaught;
    }

    public void setYearTaught(int YearTaught) {
        this.YearTaught = YearTaught;
    }
}
