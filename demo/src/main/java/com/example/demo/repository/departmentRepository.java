package com.example.demo.repository;

import com.example.demo.entity.departments;
import org.springframework.data.jpa.repository.JpaRepository;

// JpaRepository provides basic CRUD operations for User
public interface departmentRepository extends JpaRepository<departments, String> {
    // Custom query methods can be added here (optional)
}
