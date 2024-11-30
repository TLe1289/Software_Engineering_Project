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

import com.example.demo.entity.students;
import com.example.demo.repository.studentsRepository;

@RestController
@RequestMapping("/students")
public class StudentsController {

    @Autowired
    private studentsRepository studentsFolder;

    @GetMapping
    public List<students> getAllStudents() {
        return studentsFolder.findAll();
    }

    @GetMapping("/{id}")
    public students getStudentById(@PathVariable String id) {
        return studentsFolder.findById(id).orElse(null);
    }

    @PostMapping
    public students createStudent(@RequestBody students newStudent) {
        return studentsFolder.save(newStudent);
    }

    @PutMapping("/{id}")
    public students updateStudent(@PathVariable String id, @RequestBody students updatedStudent) {
        return studentsFolder.findById(id).map(existing -> {
            existing.setGender(updatedStudent.getGender());
            existing.setMajor(updatedStudent.getMajor());
            return studentsFolder.save(existing);
        }).orElse(null);
    }

    @DeleteMapping("/{id}")
    public String deleteStudent(@PathVariable String id) {
        studentsFolder.deleteById(id);
        return "Student with ID " + id + " deleted.";
    }
    
}
