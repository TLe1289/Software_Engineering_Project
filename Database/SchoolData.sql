INSERT INTO Students (StudentID, Gender, Major) VALUES 
('U1', 'F', 'CyS'),
('U2', 'F', 'MATH'),
('U3', 'M', 'EE'),
('U4', 'F', 'CyS'),
('U5', 'M', 'IT'),
('U6', 'M', 'IT'),
('U7', 'M', 'CyS'),
('U8', 'M', 'EE'),
('U9', 'F', 'CyS'),
('U10', 'F', 'MATH'),
('U11', 'M', 'IT'),
('U12', 'F', 'EE'),
('U13', 'M', 'CyS'),
('U14', 'M', 'EE'),
('U15', 'M', 'EE'),
('U16', 'F', 'IT'),
('U17', 'F', 'EDU'),
('U18', 'M', 'EDU'),
('U19', 'M', 'IT'),
('U20', 'M', 'CyS');

INSERT INTO Departments (DepartmentID, Building, Office, MajorOffered, TotalHoursReq, AdvisorID, AdvisorPhone) VALUES
('D1', 'G', '233.0', 'ART', '126.0', 'A6', '1117'),
('D2', 'R', '1045.0', 'CS', '122.0', 'A1', '2002'),
('D2', 'R', '1045.0', 'CS', '122.0', 'A2', '2324'),
('D2', 'R', '1045.0', 'IT', '124.0', 'A3', '2717'),
('D2', 'R', '1045.0', 'IT', '124.0', 'A4', '2888'),
('D2', 'R', '1045.0', 'CyS', '122.0', 'A5', '2202'),
('D2', 'R', '1045.0', 'CyS', '122.0', 'A6', '2329'),
('D2', 'R', '1045.0', 'CyS', '122.0', 'A7', '2555'),
('D2', 'R', '1045.0', 'IS', '126.0', 'A8', '2007'),
('D3', 'H', '2120.0', 'EE', '124.0', 'A17', '3090'),
('D3', 'H', '2120.0', 'EE', '124.0', 'A20', '3311'),
('D3', 'H', '2120.0', 'CpE', '126.0', 'A11', '3414'),
('D4', 'H', '1064.0', 'EDU', '120.0', 'A12', '7209'),
('D5', 'G', '118.0', 'MATH', '120.0', 'A22', '4314'),
('D5', 'G', '118.0', 'MATH', '120.0', 'A23', '4412'),
('D5', 'G', '118.0', 'MATH', '120.0', 'A25', '4887'),
('D5', 'G', '118.0', 'MEDU', '124.0', 'A14', '1445'),
('D6', 'M', '36.0', 'SOC', '120.0', 'A15', '2710'),
('D7', 'G', '104.0', 'ACCT', '122.0', 'A16', '5110'),
('D7', 'G', '104.0', 'MKT', '126.0', 'A9', '5116'),
('D8', 'M', '32.0', 'BIOL', '120.0', 'A17', '2800'),
('D9', 'H', '1152.0', 'PHY', '124.0', 'A26', '1528');

INSERT INTO Staffs (StaffID, DepartmentID, Phone) VALUES 
('F1', 'D2', '6114'),
('F2', 'D2', '6177'),
('F3', 'D5', '2111'),
('F4', 'D4', '3229'),
('F5', 'D2', '6492'),
('F6', 'D3', '3566'),
('F7', 'D5', '2090'),
('F8', 'D3', '3109'),
('F9', 'D2', '6600'),
('F10', 'D4', '2002'),
('F11', 'D8', '1664'),
('F12', 'D8', '1544'),
('F13', 'D2', '6363'),
('F14', 'D9', '3666'),
('F15', 'D5', '2919'),
('F16', 'D1', '2711'),
('F17', 'D2', '6801'),
('F18', 'D8', '2610'),
('F19', 'D1', '2451');

INSERT INTO Instructors (InstructorID, InstructorPhone, DepartmentID, HiredSemester) VALUES 
('T1', '2203', 'D2', 'F2015'),
('T2', '2219', 'D2', 'F2017'),
('T3', '5461', 'D4', 'S2017'),
('T4', '2390', 'D2', 'F2008'),
('T5', '3018', 'D2', 'F2010'),
('T6', '5517', 'D5', 'F2015'),
('T7', '2018', 'D2', 'S2015'),
('T8', '3108', 'D1', 'S2016'),
('T9', '7211', 'D3', 'F2011'),
('T10', '2653', 'D6', 'F2004'),
('T11', '4517', 'D9', 'F2010'),
('T12', '1802', 'D8', 'S2016'),
('T13', '6229', 'D7', 'S2016');

INSERT INTO InstructorCourse (InstructorID, CoursePrefix, CourseNumber, Credits, Semester, YearTaught) VALUES
('T1', 'CNT', '4104', '4', 'S', '2019'),
('T1', 'CNT', '4104', '4', 'F', '2019'),
('T1', 'CNT', '4104', '4', 'F', '2020'),
('T1', 'CNT', '4104', '4', 'S', '2021'),
('T1', 'CIS', '4935', '4', 'S', '2020'),
('T2', 'CNT', '4100', '1', 'F', '2019'),
('T2', 'CNT', '4100', '1', 'F', '2020'),
('T2', 'COP', '4703', '3', 'F', '2020'),
('T2', 'COP', '4703', '3', 'S', '2021'),
('T2', 'COP', '4703', '3', 'F', '2021'),
('T4', 'CIS', '2233', '3', 'F', '2019'),
('T4', 'CIS', '2233', '3', 'S', '2020'),
('T4', 'CIS', '2003', '3', 'S', '2020'),
('T4', 'CIS', '2003', '3', 'F', '2020'),
('T4', 'CIS', '3433', '3', 'F', '2019'),
('T4', 'CIS', '3433', '3', 'F', '2020'),
('T4', 'CIS', '4935', '4', 'U', '2020'),
('T4', 'CIS', '4935', '4', 'F', '2020'),
('T5', 'CIS', '2233', '3', 'S', '2019'),
('T5', 'CIS', '2233', '3', 'U', '2019'),
('T5', 'CIS', '4935', '4', 'S', '2019'),
('T7', 'COP', '2512', '3', 'S', '2019'),
('T7', 'COP', '2512', '3', 'S', '2020'),
('T7', 'COP', '2512', '3', 'F', '2020'),
('T7', 'COP', '4703', '3', 'S', '2019'),
('T7', 'COP', '4703', '3', 'S', '2020'),
('T7', 'COP', '4703', '3', 'F', '2019'),
('T7', 'CIS', '4935', '4', 'U', '2019'),
('T7', 'CIS', '4935', '4', 'S', '2021'),
('T8', 'ARH', '3001', '1', 'F', '2019'),
('T8', 'ARH', '3001', '1', 'S', '2020'),
('T8', 'ARH', '3001', '1', 'U', '2020'),
('T8', 'ARH', '3001', '1', 'S', '2021'),
('T8', 'ART', '3635', '3', 'F', '2019'),
('T8', 'ART', '3635', '3', 'F', '2020'),
('T8', 'ART', '3635', '3', 'F', '2021'),
('T9', 'EGN', '3420', '1', 'S', '2019'),
('T9', 'EGN', '3420', '1', 'U', '2019'),
('T9', 'EGN', '3420', '1', 'S', '2020'),
('T9', 'EGN', '3420', '1', 'S', '2021'),
('T9', 'EEL', '4914', '4', 'S', '2019'),
('T9', 'EEL', '4914', '4', 'F', '2019'),
('T9', 'EEL', '4914', '4', 'F', '2020'),
('T9', 'EEL', '4914', '4', 'S', '2021'),
('T11', 'PHY', '2048', '3', 'U', '2019'),
('T11', 'PHY', '2048', '3', 'F', '2019'),
('T11', 'PHY', '2048', '3', 'F', '2020'),
('T11', 'PHY', '2048', '3', 'S', '2021'),
('T12', 'ZOO', '1404', '1', 'S', '2019'),
('T12', 'ZOO', '1404', '1', 'F', '2019'),
('T12', 'ZOO', '1404', '1', 'S', '2020'),
('T12', 'ZOO', '1404', '1', 'F', '2020'),
('T12', 'ZOO', '1404', '1', 'U', '2021');

INSERT INTO StudentCourse (StudentID, CoursePrefix, CourseNumber, Semester, YearTaken, Grade) VALUES
('U1', 'CIS', '2233', 'F', '2019', 'A'),
('U1', 'EGN', '3420', 'S', '2019', 'B'),
('U1', 'CNT', '4104', 'S', '2021', 'A'),
('U1', 'CNT', '4100', 'F', '2019', 'B'),
('U1', 'COP', '4703', 'S', '2020', 'C'),
('U3', 'ARH', '3001', 'S', '2021', 'B'),
('U3', 'ZOO', '1404', 'S', '2019', 'A'),
('U3', 'EEL', '4914', 'F', '2019', 'A'),
('U5', 'EGN', '3420', 'S', '2019', 'B'),
('U5', 'PHY', '2048', 'U', '2019', 'F'),
('U5', 'CNT', '4104', 'S', '2021', 'C'),
('U5', 'CIS', '4935', 'S', '2021', 'C'),
('U5', 'COP', '2512', 'S', '2020', 'C'),
('U5', 'ART', '3635', 'F', '2019', 'A'),
('U5', 'CIS', '3433', 'F', '2020', 'A'),
('U5', 'CIS', '2003', 'F', '2020', 'B'),
('U6', 'COP', '4703', 'S', '2020', 'A'),
('U6', 'CIS', '4935', 'S', '2021', 'A'),
('U6', 'CIS', '3433', 'F', '2020', 'A'),
('U7', 'CIS', '2233', 'F', '2019', 'A'),
('U7', 'ZOO', '1404', 'S', '2019', 'A'),
('U7', 'CNT', '4100', 'F', '2019', 'C'),
('U7', 'COP', '4703', 'S', '2020', 'B'),
('U7', 'ARH', '3001', 'U', '2020', 'A'),
('U7', 'CIS', '2003', 'F', '2020', 'C'),
('U7', 'COP', '2512', 'S', '2020', 'D'),
('U7', 'CIS', '4935', 'S', '2021', 'B'),
('U9', 'CIS', '2233', 'F', '2019', 'F'),
('U9', 'CIS', '2233', 'S', '2020', 'C'),
('U9', 'ARH', '3001', 'S', '2021', 'C'),
('U9', 'ZOO', '1404', 'S', '2019', 'B'),
('U9', 'CNT', '4104', 'S', '2021', 'B'),
('U9', 'COP', '4703', 'F', '2019', 'B'),
('U9', 'CIS', '4935', 'S', '2021', 'A'),
('U11', 'ZOO', '1404', 'F', '2020', 'A'),
('U11', 'ART', '3635', 'F', '2019', 'A'),
('U11', 'COP', '2512', 'S', '2019', 'I'),
('U11', 'COP', '2512', 'S', '2020', 'D'),
('U11', 'COP', '2512', 'F', '2020', 'A'),
('U11', 'CIS', '4935', 'S', '2021', 'B'),
('U11', 'CIS', '3433', 'F', '2019', 'C'),
('U11', 'CNT', '4104', 'S', '2021', 'A'),
('U12', 'ARH', '3001', 'S', '2021', 'B'),
('U12', 'EGN', '3420', 'S', '2019', 'B'),
('U12', 'PHY', '2048', 'U', '2019', 'D'),
('U12', 'EEL', '4914', 'F', '2019', 'A'),
('U12', 'COP', '2512', 'S', '2020', 'A'),
('U13', 'CNT', '4104', 'S', '2021', 'B'),
('U13', 'CIS', '4935', 'U', '2019', 'F'),
('U13', 'CIS', '4935', 'S', '2021', 'D'),
('U13', 'COP', '2512', 'S', '2020', 'C'),
('U13', 'PHY', '2048', 'S', '2021', 'C'),
('U14', 'EEL', '4914', 'S', '2019', 'B'),
('U14', 'EGN', '3420', 'S', '2021', 'B'),
('U14', 'PHY', '2048', 'U', '2019', 'B'),
('U17', 'PHY', '2048', 'U', '2019', 'A'),
('U17', 'ART', '3635', 'F', '2021', 'A'),
('U20', 'ZOO', '1404', 'U', '2021', 'B'),
('U20', 'COP', '4703', 'F', '2019', 'B'),
('U20', 'ART', '3635', 'F', '2019', 'A'),
('U20', 'CIS', '3433', 'F', '2019', 'B'),
('U20', 'CIS', '2003', 'S', '2020', 'F'),
('U20', 'CIS', '2003', 'F', '2020', 'B');