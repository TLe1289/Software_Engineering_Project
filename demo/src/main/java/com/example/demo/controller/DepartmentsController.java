package com.example.demo.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.demo.entity.departments;
import com.example.demo.repository.departmentRepository;




@RestController
@RequestMapping("/departments")

public class DepartmentsController{

    @Autowired
    private departmentRepository departmentFolder;

    @GetMapping
    public List<departments> getALLDepartments(){
        return departmentFolder.findAll();
    }

    @GetMapping("/{id}")
    public departments getDepartmentbyID(@PathVariable String id){
        return departmentFolder.findById(id).orElse(null);
    }

    @PostMapping
    public departments createDepartments(@RequestBody departments one){
        return departmentFolder.save(one);
    }

    @PutMapping("/{id}")
    public departments updateDepartments(@PathVariable String id, @RequestBody departments updatedDepartments){
        return departmentFolder.findById(id).map(thing -> {
        thing.setDepartmentID(thing.getDepartmentID());
        thing.setBuilding(thing.getBuilding());
        thing.setMajorOffered(thing.getMajorOffered());
        thing.setTotalHoursReq(thing.getTotalHoursReq());
        thing.setAdvisorID(thing.getAdvisorID());
        thing.setAdvisorPhone(thing.getAdvisorPhone());
        return departmentFolder.save(thing);
        }).orElse(null);
    }
    
    @DeleteMapping("/{id}")
    public String deleteUser(@PathVariable String id){
        departmentFolder.deleteById(id);
        return "USer with ID" + id + " deleted.";
    }
    
    

}

