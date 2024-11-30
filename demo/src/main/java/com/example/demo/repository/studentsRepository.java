package com.example.demo.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.example.demo.entity.students;

// JpaRepository provides basic CRUD operations for Students
public interface studentsRepository extends JpaRepository<students, String> {
    
}
