package com.example.demo.entity;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;


@Entity
@Table(name = "instructors")
public class instructors {

    @Id
    private String InstructorID;
    private int InstructorPhone;
    private String DepartmentID;
    private String HiredSemester;

    // Getters and Setters

    public String getInstructorID() {
        return InstructorID;
    }

    public void setInstructorID(String InstructorID) {
        this.InstructorID = InstructorID;
    }

    public int getInstructorPhone() {
        return InstructorPhone;
    }

    public void setInstructorPhone(int InstructorPhone) {
        this.InstructorPhone = InstructorPhone;
    }

    public String getDepartmentID() {
        return DepartmentID;
    }

    public void setDepartmentID(String DepartmentID) {
        this.DepartmentID = DepartmentID;
    }

    public String getHiredSemester() {
        return HiredSemester;
    }

    public void setHiredSemester(String HiredSemester) {
        this.HiredSemester = HiredSemester;
    }
}
