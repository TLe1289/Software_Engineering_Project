package com.example.demo.entity;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;


@Entity
@Table(name = "students")
public class students {

    @Id
    private String StudentID;
    private char Gender;
    private String Major;

    // Getters and Setters

    public String getStudentID() {
        return StudentID;
    }

    public void setStudentID(String StudentID) {
        this.StudentID = StudentID;
    }

    public char getGender() {
        return Gender;
    }

    public void setGender(char Gender) {
        this.Gender = Gender;
    }

    public String getMajor() {
        return Major;
    }

    public void setMajor(String Major) {
        this.Major = Major;
    }
}
