package com.example.demo.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.demo.entity.studentcourse;
import com.example.demo.repository.studentcourseRepository;

@RestController
@RequestMapping("/studentcourses")
public class StudentCourseController {

    @Autowired
    private studentcourseRepository studentcourseFolder;

    @GetMapping
    public List<studentcourse> getAllStudentCourses() {
        return studentcourseFolder.findAll();
    }

    @PostMapping
    public studentcourse createStudentCourse(@RequestBody studentcourse newStudentCourse) {
        return studentcourseFolder.save(newStudentCourse);
    }

    @DeleteMapping("/{id}")
    public String deleteStudentCourse(@PathVariable String id) {
        studentcourseFolder.deleteById(id);
        return "StudentCourse entry with ID " + id + " deleted.";
    }
}
