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

import com.example.demo.entity.instructors;
import com.example.demo.repository.instructorsRepository;

@RestController
@RequestMapping("/instructors")
public class InstructorsController {

    @Autowired
    private instructorsRepository instructorsFolder;

    @GetMapping
    public List<instructors> getAllInstructors() {
        return instructorsFolder.findAll();
    }

    @GetMapping("/{id}")
    public instructors getInstructorById(@PathVariable String id) {
        return instructorsFolder.findById(id).orElse(null);
    }

    @PostMapping
    public instructors createInstructor(@RequestBody instructors newInstructor) {
        return instructorsFolder.save(newInstructor);
    }

    @PutMapping("/{id}")
    public instructors updateInstructor(@PathVariable String id, @RequestBody instructors updatedInstructor) {
        return instructorsFolder.findById(id).map(existing -> {
            existing.setInstructorPhone(updatedInstructor.getInstructorPhone());
            existing.setDepartmentID(updatedInstructor.getDepartmentID());
            existing.setHiredSemester(updatedInstructor.getHiredSemester());
            return instructorsFolder.save(existing);
        }).orElse(null);
    }

    @DeleteMapping("/{id}")
    public String deleteInstructor(@PathVariable String id) {
        instructorsFolder.deleteById(id);
        return "Instructor with ID " + id + " deleted.";
    }
}
