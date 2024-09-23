import React, { useState } from 'react';
import './AdvisorDashboard.css';

const AdvisorDashboard = () => {
  const [showSearchModal, setShowSearchModal] = useState(false); // Controls the first modal (search bar)
  const [showScheduleModal, setShowScheduleModal] = useState(false); // Controls the second modal (class schedule)
  const [studentId, setStudentId] = useState(''); // Stores the entered student ID
  const [searchError, setSearchError] = useState(''); // Stores search errors
  const [selectedActions, setSelectedActions] = useState({}); // Stores selected actions for each course

  // Dummy student data
  const dummyStudent = {
    id: 'S123456',
    name: 'John Doe',
    courses: [
      { coursePrefix: 'CS', courseNumber: '101', semester: 'Fall', yearTaken: '2022' },
      { coursePrefix: 'CS', courseNumber: '102', semester: 'Spring', yearTaken: '2023' },
    ]
  };

  // Function to toggle the search modal
  const toggleSearchModal = () => {
    setShowSearchModal(!showSearchModal);
    setSearchError('');
  };

  // Function to search for student
  const handleSearch = () => {
    if (studentId === dummyStudent.id) {
      setShowScheduleModal(true); // Show class schedule if student is found
      setShowSearchModal(false); // Close search modal
    } else {
      setSearchError('Student not found. Please enter a valid Student ID.');
    }
  };

  // Function to toggle the class schedule modal
  const toggleScheduleModal = () => {
    setShowScheduleModal(!showScheduleModal);
  };

  // Handle change for the action (Add or Drop) in the table
  const handleActionChange = (courseNumber, action) => {
    setSelectedActions((prevState) => ({
      ...prevState,
      [courseNumber]: action
    }));
  };

  return (
    <>
      {/* Section 1: Advisor Information */}
      <div className="container">
        <h2>Advisor Information</h2>
        <p><strong>Advisor ID:</strong> A123456</p>
        <p><strong>Phone Number:</strong> +123456789</p>
        <p><strong>Department ID:</strong> D001</p>
        <p><strong>Department Room:</strong> Room 204</p>
        <p><strong>Building:</strong> Science Building</p>
        <p><strong>Major Advised:</strong> Computer Science</p>
        <p><strong>Total Hours Required for Major:</strong> 120</p>
      </div>

      {/* Section 2: Add/Drop Button */}
      <div className="container">
        <h2>Manage Enrollments</h2>
        <button className="search-btn" onClick={toggleSearchModal}>
          Add / Drop Course
        </button>
      </div>

      {/* Modal for Searching Student */}
      {showSearchModal && (
        <div className="modal-overlay">
          <div className="modal-content">
            <h3>Enter Student ID</h3>
            <input
              type="text"
              placeholder="Enter Student ID"
              value={studentId}
              onChange={(e) => setStudentId(e.target.value)}
              className="student-id-input"
            />
            {searchError && <p className="error">{searchError}</p>}
            <button className="search-btn" onClick={handleSearch}>
              Search
            </button>
            <button className="close-btn" onClick={toggleSearchModal}>
              Close
            </button>
          </div>
        </div>
      )}

      {/* Modal for Student Class Schedule */}
      {showScheduleModal && (
        <div className="modal-overlay">
          <div className="modal-content">
            <h3>Student: {dummyStudent.name} (ID: {dummyStudent.id})</h3>
            <div className="table-wrapper">
              <table className="courses-table">
                <thead>
                  <tr>
                    <th>Course Prefix</th>
                    <th>Course Number</th>
                    <th>Semester</th>
                    <th>Year Taken</th>
                    <th>Action</th>
                  </tr>
                </thead>
                <tbody>
                  {dummyStudent.courses.map((course, index) => (
                    <tr key={index}>
                      <td>{course.coursePrefix}</td>
                      <td>{course.courseNumber}</td>
                      <td>{course.semester}</td>
                      <td>{course.yearTaken}</td>
                      <td>
                        <select
                          className={`action-select ${
                            selectedActions[course.courseNumber] === 'add'
                              ? 'add-selected'
                              : selectedActions[course.courseNumber] === 'drop'
                              ? 'drop-selected'
                              : ''
                          }`}
                          value={selectedActions[course.courseNumber] || ''}
                          onChange={(e) =>
                            handleActionChange(course.courseNumber, e.target.value)
                          }
                        >
                          <option value="">Select</option>
                          <option value="add" className="add-btn">Add</option>
                          <option value="drop" className="drop-btn">Drop</option>
                        </select>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>

            <button className="submit-change-btn">Submit Change</button>
            <button className="close-btn" onClick={toggleScheduleModal}>
              Close
            </button>
          </div>
        </div>
      )}


  
    </>
  );
};

export default AdvisorDashboard;
