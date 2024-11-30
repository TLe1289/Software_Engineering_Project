package com.example.demo.entity;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;


@Entity
@Table(name = "departments")
public class departments {

    @Id
    private String DepartmentID;
    private String Building;
    private int Office;
    private String MajorOffered;
    private int TotalHoursReq;
    private String AdvisorID;
    private int AdvisorPhone;


    // Getters and setters

    public String getDepartmentID() { return DepartmentID; }
    public void setDepartmentID(String DepartmentID) { this.DepartmentID = DepartmentID; }

    public String getBuilding() { return Building; }
    public void setBuilding(String Building) {this.Building = Building;}

    public int getOffice() {return Office;}
    public void setOffice(int Office) {this.Office = Office; }

    public String getMajorOffered() { return MajorOffered; }
    public void setMajorOffered(String MajorOffered) {this.MajorOffered = MajorOffered;}

    public int getTotalHoursReq() {return TotalHoursReq;}
    public void setTotalHoursReq(int TotalHoursReq) {this.TotalHoursReq = TotalHoursReq; }

    public String getAdvisorID() {return AdvisorID;}
    public void setAdvisorID(String AdvisorID) {this.AdvisorID = AdvisorID;}

    public int getAdvisorPhone() {return AdvisorPhone;}
    public void setAdvisorPhone(int AdvisorPhone) {this.AdvisorPhone = AdvisorPhone;} 
}