package com.example.demo.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.example.demo.entity.studentcourse;

// JpaRepository provides basic CRUD operations for StudentCourse
public interface studentcourseRepository extends JpaRepository<studentcourse, String> {
   
}

