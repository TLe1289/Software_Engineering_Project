package com.example.demo.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.example.demo.entity.instructorcourse;

// JpaRepository provides basic CRUD operations for InstructorCourse
public interface instructorcourseRepository extends JpaRepository<instructorcourse, String> {
    
}
