USE SchoolDatabase;

DELIMITER $$

CREATE TRIGGER PopulateCreditsBeforeInsert
BEFORE INSERT ON StudentCourse
FOR EACH ROW
BEGIN
    DECLARE courseCredits INT;

    -- Find the credits for the course from InstructorCourse
    SELECT InstructorCourse.InstructorCredits INTO courseCredits
    FROM InstructorCourse
    WHERE InstructorCourse.CoursePrefix = NEW.CoursePrefix
      AND InstructorCourse.CourseNumber = NEW.CourseNumber
      AND InstructorCourse.Semester = NEW.Semester
      AND InstructorCourse.YearTaught = NEW.YearTaken
    LIMIT 1;

    -- Set the Credits column in the NEW record
    SET NEW.Credits = courseCredits;
END$$

DELIMITER ;






DELIMITER $$

CREATE TRIGGER UpdateStudentGPAAndCredits
AFTER INSERT ON StudentCourse
FOR EACH ROW
BEGIN
    DECLARE totalGradePoints DECIMAL(10, 2);
    DECLARE totalCredits INT;

    -- Calculate total grade points (credits * grade point)
    SELECT SUM(Credits * 
               CASE NEW.Grade
                   WHEN 'A' THEN 4.0
                   WHEN 'B' THEN 3.0
                   WHEN 'C' THEN 2.0
                   WHEN 'D' THEN 1.0
                   ELSE 0.0
               END)
    INTO totalGradePoints
    FROM StudentCourse
    WHERE StudentID = NEW.StudentID;

    -- Calculate total credits
    SELECT SUM(Credits)
    INTO totalCredits
    FROM StudentCourse
    WHERE StudentID = NEW.StudentID;

    -- Update the GPA and CreditsTaken in the Students table
    UPDATE Students
    SET 
        GPA = CASE 
                WHEN totalCredits > 0 THEN totalGradePoints / totalCredits
                ELSE 0.0
             END,
        CreditsTaken = totalCredits
    WHERE StudentID = NEW.StudentID;
END$$

DELIMITER ;
