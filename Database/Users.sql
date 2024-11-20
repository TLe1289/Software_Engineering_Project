CREATE USER 'Staff'@'%' IDENTIFIED BY 'password123';
CREATE USER 'Advisor'@'%' IDENTIFIED BY 'password123';
CREATE USER 'Student'@'%' IDENTIFIED BY 'password123';
CREATE USER 'Instructor'@'%' IDENTIFIED BY 'password123';

CREATE ROLE 'Staff', 'Advisor', 'Student', 'Instructor';

GRANT 'Staff' TO 'Staff'@'%';
GRANT 'Advisor' TO 'Advisor'@'%';
GRANT 'Instructor' TO 'Instructor'@'%';
GRANT 'Student' TO 'Student'@'%';


GRANT SELECT, INSERT, UPDATE, DELETE ON SchoolDatabase.Departments TO 'Staff'; --Note: Needs restriction (See Requirement 1)
GRANT SELECT, INSERT, UPDATE, DELETE ON SchoolDatabase.InstructorCourse TO 'Staff';
GRANT SELECT, INSERT, UPDATE, DELETE ON SchoolDatabase.StudentCourse TO 'Staff';
GRANT SELECT, INSERT, UPDATE, DELETE ON SchoolDatabase.Instructors TO 'Staff';
GRANT SELECT, INSERT, UPDATE, DELETE ON SchoolDatabase.Students TO 'Staff';

GRANT SELECT, INSERT, UPDATE, DELETE ON SchoolDatabase.StudentCourse TO 'Advisor'; --Note: Advisor's ability to do this should be severely limited (See Requirement 2)

