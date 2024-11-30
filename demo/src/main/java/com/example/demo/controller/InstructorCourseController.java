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

import com.example.demo.entity.instructorcourse;
import com.example.demo.repository.instructorcourseRepository;

@RestController
@RequestMapping("/instructorcourses")
public class InstructorCourseController {

    @Autowired
    private instructorcourseRepository instructorcourseFolder;

    @GetMapping
    public List<instructorcourse> getAllInstructorCourses() {
        return instructorcourseFolder.findAll();
    }

    @PostMapping
    public instructorcourse createInstructorCourse(@RequestBody instructorcourse newInstructorCourse) {
        return instructorcourseFolder.save(newInstructorCourse);
    }

    @DeleteMapping("/{id}")
    public String deleteInstructorCourse(@PathVariable String id) {
        instructorcourseFolder.deleteById(id);
        return "InstructorCourse entry with ID " + id + " deleted.";
    }
}
