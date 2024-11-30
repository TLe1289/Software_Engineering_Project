package com.example.demo.entity;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;


@Entity
@Table(name = "staffs")
public class staffs {

    @Id
    private String StaffID;
    private String DepartmentID;
    private int Phone;

    // Getters and Setters

    public String getStaffID() {
        return StaffID;
    }

    public void setStaffID(String StaffID) {
        this.StaffID = StaffID;
    }

    public String getDepartmentID() {
        return DepartmentID;
    }

    public void setDepartmentID(String DepartmentID) {
        this.DepartmentID = DepartmentID;
    }

    public int getPhone() {
        return Phone;
    }

    public void setPhone(int Phone) {
        this.Phone = Phone;
    }
}
