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

import com.example.demo.entity.staffs;
import com.example.demo.repository.staffsRepository;

@RestController
@RequestMapping("/staffs")
public class StaffsController {

    @Autowired
    private staffsRepository staffsFolder;

    @GetMapping
    public List<staffs> getAllStaffs() {
        return staffsFolder.findAll();
    }

    @GetMapping("/{id}")
    public staffs getStaffById(@PathVariable String id) {
        return staffsFolder.findById(id).orElse(null);
    }

    @PostMapping
    public staffs createStaff(@RequestBody staffs newStaff) {
        return staffsFolder.save(newStaff);
    }

    @PutMapping("/{id}")
    public staffs updateStaff(@PathVariable String id, @RequestBody staffs updatedStaff) {
        return staffsFolder.findById(id).map(existing -> {
            existing.setDepartmentID(updatedStaff.getDepartmentID());
            existing.setPhone(updatedStaff.getPhone());
            return staffsFolder.save(existing);
        }).orElse(null);
    }

    @DeleteMapping("/{id}")
    public String deleteStaff(@PathVariable String id) {
        staffsFolder.deleteById(id);
        return "Staff with ID " + id + " deleted.";
    }
}
