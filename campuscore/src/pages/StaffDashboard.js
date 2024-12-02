import React, { useState } from 'react';
import './StaffDashboard.css'; // Import the staff dashboard-specific styles

const StaffDashboard = () => {
  const [showSearchModal, setShowSearchModal] = useState(false); // Controls the first modal (search bar)
  const [showAssignModal, setShowAssignModal] = useState(false); // Controls the assign instructor modal
  const [showModifyDepartmentModal, setShowModifyDepartmentModal] = useState(false); // Controls the department modification modal
  const [showModifyCourseModal, setShowModifyCourseModal] = useState(false); // Controls the course modification modal
  const [instructorId, setInstructorId] = useState(''); // Stores the entered instructor ID
  const [searchError, setSearchError] = useState(''); // Stores search errors
  const [selectedActions, setSelectedActions] = useState({}); // Stores selected actions for each course

  // Dummy instructor data
  const dummyInstructor = {
    id: 'I123456',
    name: 'Jane Doe',
  };

  // Dummy course data for Modify Course Info
  const dummyCourse = {
    prefix: 'CS',
    number: '201',
    credit: 3,
    semester: 'Fall',
    year: '2022',
  };

  // Toggle Search Modal
  const toggleSearchModal = () => {
    setShowSearchModal(!showSearchModal);
    setSearchError('');
  };

  // Toggle Assign Modal
  const toggleAssignModal = () => {
    setShowAssignModal(!showAssignModal);
  };

  // Toggle Modify Department Info Modal
  const toggleModifyDepartmentModal = () => {
    setShowModifyDepartmentModal(!showModifyDepartmentModal);
  };

  // Toggle Modify Course Info Modal
  const toggleModifyCourseModal = () => {
    setShowModifyCourseModal(!showModifyCourseModal);
  };

  // Handle instructor search
  const handleSearch = () => {
    if (instructorId === dummyInstructor.id) {
      setShowAssignModal(true); // Show assignment modal if instructor is found
      setShowSearchModal(false); // Close search modal
    } else {
      setSearchError('Instructor not found. Please enter a valid Instructor ID.');
    }
  };

  // Handle action change for the course assignment (Add/Remove)
  const handleActionChange = (courseNumber, action) => {
    setSelectedActions((prevState) => ({
      ...prevState,
      [courseNumber]: action
    }));
  };

  return (
    <>
      {/* Section 1: Manage Courses */}
      <div className="staff-info-container">
        <h2>Manage Courses</h2>
        <button className="add-course-btn" onClick={toggleSearchModal}>
          Add Course
        </button>
        <button className="remove-course-btn" onClick={toggleSearchModal}>
          Remove Course
        </button>
      </div>

      {/* Section 2: Assign Instructors */}
      <div className="staff-info-container">
        <h2>Assign Instructors</h2>
        <button className="assign-instructor-btn" onClick={toggleSearchModal}>
          Assign Instructor
        </button>
      </div>

      {/* Section 3: Modify Course Info */}
      <div className="staff-info-container">
        <h2>Modify Course Info</h2>
        <button className="modify-course-btn" onClick={toggleModifyCourseModal}>
          Modify Course Info
        </button>
      </div>

      {/* Section 4: Department Information */}
      <div className="staff-info-container">
        <h2>Department Information</h2>
        <p>Details about the department will be displayed here...</p>
        <button className="modify-department-btn" onClick={toggleModifyDepartmentModal}>
          Modify Department Info
        </button>
      </div>

      {/* Search Instructor Modal */}
      {showSearchModal && (
        <div className="modal-overlay">
          <div className="modal-content">
            <h3>Enter Instructor ID</h3>
            <input
              type="text"
              placeholder="Enter Instructor ID"
              value={instructorId}
              onChange={(e) => setInstructorId(e.target.value)}
              className="instructor-id-input"
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

      {/* Assign Instructor Modal */}
      {showAssignModal && (
        <div className="modal-overlay">
          <div className="modal-content">
            <h3>Assign Courses for Instructor: {dummyInstructor.name} (ID: {dummyInstructor.id})</h3>
            <div className="courses-container">
              <table className="courses-table">
                <thead>
                  <tr>
                    <th>Course Prefix</th>
                    <th>Course Number</th>
                    <th>Credits</th>
                    <th>Semester</th>
                    <th>Year</th>
                    <th>Action</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><input type="text" placeholder="Enter Course Prefix" /></td>
                    <td><input type="text" placeholder="Enter Course Number" /></td>
                    <td><input type="text" placeholder="Enter Credits" /></td>
                    <td><input type="text" placeholder="Enter Semester" /></td>
                    <td><input type="text" placeholder="Enter Year" /></td>
                    <td>
                      <select
                        className="action-select"
                        value={selectedActions['assign'] || ''}
                        onChange={(e) => handleActionChange('assign', e.target.value)}
                      >
                        <option value="">Select</option>
                        <option value="add">Add</option>
                        <option value="remove">Remove</option>
                      </select>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
            <button className="submit-change-btn">Submit Change</button>
            <button className="close-btn" onClick={toggleAssignModal}>
              Close
            </button>
          </div>
        </div>
      )}

      {/* Modify Course Info Modal */}
      {showModifyCourseModal && (
        <div className="modal-overlay">
          <div className="modal-content">
            <h3>Modify Course Information</h3>
            <div className="courses-container">
              <table className="courses-table">
                <thead>
                  <tr>
                    <th>Course Prefix</th>
                    <th>Course Number</th>
                    <th>Credits</th>
                    <th>Semester</th>
                    <th>Year</th>
                    <th>Action</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><input type="text" placeholder="Enter Course Prefix" defaultValue={dummyCourse.prefix} /></td>
                    <td><input type="text" placeholder="Enter Course Number" defaultValue={dummyCourse.number} /></td>
                    <td><input type="text" placeholder="Enter Credits" defaultValue={dummyCourse.credit} /></td>
                    <td><input type="text" placeholder="Enter Semester" defaultValue={dummyCourse.semester} /></td>
                    <td><input type="text" placeholder="Enter Year" defaultValue={dummyCourse.year} /></td>
                    <td>
                      <select
                        className={`action-select ${
                          selectedActions[dummyCourse.number] === 'add'
                            ? 'add-selected'
                            : selectedActions[dummyCourse.number] === 'remove'
                            ? 'remove-selected'
                            : ''
                        }`}
                        value={selectedActions[dummyCourse.number] || ''}
                        onChange={(e) => handleActionChange(dummyCourse.number, e.target.value)}
                      >
                        <option value="">Select</option>
                        <option value="add">Add</option>
                        <option value="remove">Remove</option>
                      </select>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
            <button className="submit-change-btn">Submit Change</button>
            <button className="close-btn" onClick={toggleModifyCourseModal}>
              Close
            </button>
          </div>
        </div>
      )}

      {/* Modify Department Info Modal */}
      {showModifyDepartmentModal && (
        <div className="modal-overlay">
          <div className="modal-content">
            <h3>Modify Department Information</h3>
            <div className="courses-container">
              <table className="courses-table">
                <thead>
                  <tr>
                    <th>Building</th>
                    <th>Office</th>
                    <th>Total Hours Required</th>
                    <th>Advisor ID</th>
                    <th>Advisor Phone</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><input type="text" placeholder="Enter Building" /></td>
                    <td><input type="text" placeholder="Enter Office" /></td>
                    <td><input type="text" placeholder="Enter Hours" /></td>
                    <td><input type="text" placeholder="Enter Advisor ID" /></td>
                    <td><input type="text" placeholder="Enter Phone" /></td>
                  </tr>
                </tbody>
              </table>
            </div>
            <button className="submit-change-btn">Submit Change</button>
            <button className="close-btn" onClick={toggleModifyDepartmentModal}>
              Close
            </button>
          </div>
        </div>
      )}
    </>
  );
};

export default StaffDashboard;
