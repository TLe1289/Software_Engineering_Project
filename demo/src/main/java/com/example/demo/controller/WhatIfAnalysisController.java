package com.example.demo.controller;

import java.util.HashMap;
import java.util.Map;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/what-if")
public class WhatIfAnalysisController {

@PostMapping("/scenario1")
public ResponseEntity<?> calculateScenario1(@RequestBody Map<String, Object> payload) {
    try {
        // Extract and validate input data
        Double currentGPA = payload.get("currentGPA") != null ? Double.parseDouble(payload.get("currentGPA").toString()) : null;
        Integer numCoursesTaken = payload.get("numCoursesTaken") != null ? Integer.parseInt(payload.get("numCoursesTaken").toString()) : null;
        Integer numCourses = payload.get("numCourses") != null ? Integer.parseInt(payload.get("numCourses").toString()) : null;
        Integer creditsPerCourse = payload.get("creditsPerCourse") != null ? Integer.parseInt(payload.get("creditsPerCourse").toString()) : null;
        String averageGrade = (String) payload.get("averageGrade");

        // Validate inputs
        if (currentGPA == null || numCoursesTaken == null || numCourses == null || creditsPerCourse == null || averageGrade == null) {
            return ResponseEntity.badRequest().body("Missing or invalid input fields.");
        }

        // Convert grade to numeric value
        double gradeValue = gradeToNumeric(averageGrade);

        // Calculate total quality points from the new courses
        double newQualityPoints = numCourses * creditsPerCourse * gradeValue;

        // Example calculation (simplified for demonstration purposes)
        double totalCredits = (numCoursesTaken + numCourses) * creditsPerCourse;
        double newGPA = (currentGPA * (numCoursesTaken * creditsPerCourse) + newQualityPoints) / totalCredits;

        // Prepare response
        Map<String, Object> response = new HashMap<>();
        response.put("newGPA", newGPA);

        return ResponseEntity.ok(response);

    } catch (NumberFormatException e) {
    return ResponseEntity.badRequest().body("Invalid number format. Please check your inputs.");
} catch (IllegalArgumentException e) {
    return ResponseEntity.badRequest().body("Error with provided inputs. Please ensure they are valid.");
}
}



@PostMapping("/scenario2")
public ResponseEntity<?> calculateScenario2(@RequestBody Map<String, Object> payload) {
    try {
        // Extract and validate input data
        Double currentGPA = Double.valueOf(payload.get("currentGPA").toString());
        Double desiredGPA = Double.valueOf(payload.get("desiredGPA").toString());
        Integer numCoursesTaken = Integer.valueOf(payload.get("numCoursesTaken").toString());
        Integer creditsPerCourse = Integer.valueOf(payload.get("creditsPerCourse").toString());
        String averageGrade = (String) payload.get("averageGrade");

        // Validate inputs
        if (currentGPA == null || desiredGPA == null || numCoursesTaken == null || creditsPerCourse == null || averageGrade == null) {
            return ResponseEntity.badRequest().body("Missing or invalid input fields.");
        }

        // Convert grade to numeric value
        double gradeValue = gradeToNumeric(averageGrade);

        // Calculate the total quality points needed to reach the desired GPA
        double currentQualityPoints = currentGPA * numCoursesTaken * creditsPerCourse;
        double desiredQualityPoints = desiredGPA * (numCoursesTaken + 1) * creditsPerCourse;
        double additionalQualityPointsNeeded = desiredQualityPoints - currentQualityPoints;

        // Calculate the number of courses required
        int numCoursesRequired = (int) Math.ceil(additionalQualityPointsNeeded / (creditsPerCourse * gradeValue));

        // Prepare the response
        Map<String, Object> response = new HashMap<>();
        response.put("numCoursesRequired", numCoursesRequired);

        return ResponseEntity.ok(response);

    } catch (NumberFormatException e) {

        return ResponseEntity.badRequest().body("Invalid number format. Please check your inputs.");
    } catch (IllegalArgumentException e) {
        return ResponseEntity.badRequest().body("Error with provided inputs. Please ensure they are valid.");
    }
}




    // Helper method to convert grades to numeric values
    private double gradeToNumeric(String grade) {
        switch (grade.toUpperCase()) {
            case "A" -> {
                return 4.0;
            }
            case "B" -> {
                return 3.0;
            }
            case "C" -> {
                return 2.0;
            }
            case "D" -> {
                return 1.0;
            }
            case "F" -> {
                return 0.0;
            }
            default -> throw new IllegalArgumentException("Invalid grade: " + grade);
        }
    }
}
