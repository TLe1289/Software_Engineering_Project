package com.example.demo.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.example.demo.entity.instructors;

// JpaRepository provides basic CRUD operations for Instructors
public interface instructorsRepository extends JpaRepository<instructors, String> {
    // Custom query methods can be added here (optional)
}
