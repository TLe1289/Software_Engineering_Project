package com.example.demo.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.example.demo.entity.staffs;

// JpaRepository provides basic CRUD operations for Staffs
public interface staffsRepository extends JpaRepository<staffs, String> {
    // Custom query methods can be added here (optional)
}
