import React, { useState } from 'react';
import './StudentDashboard.css'; // Import dashboard-specific styles

const StudentDashboard = () => {
  const [showModal, setShowModal] = useState(false);

  const toggleModal = () => {
    setShowModal(!showModal);
  };

  return (
    <>
      {/* Section 1: Student Information */}
<div className="container">
  <h2>Student Information</h2>
  <p><strong>Student ID:</strong> U123456</p>
  <p><strong>Gender:</strong> Male</p>
  <p><strong>Major:</strong> Computer Science</p>
  <p><strong>Current GPA:</strong> 3.5</p>
</div>

{/* Section 2: Courses Taken */}
<div className="container">
  <h2>Courses Taken</h2>
  <table className="courses-table">
    <thead>
      <tr>
        <th>Course Prefix</th>
        <th>Course Number</th>
        <th>Semester</th>
        <th>Year Taken</th>
        <th>Grade</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>CS</td>
        <td>101</td>
        <td>Fall</td>
        <td>2022</td>
        <td>A</td>
      </tr>
      <tr>
        <td>CS</td>
        <td>102</td>
        <td>Spring</td>
        <td>2023</td>
        <td>B</td>
      </tr>
      {/* Add more rows as needed */}
    </tbody>
  </table>
</div>

{/* Section 3: What-If GPA Analysis */}
<div className="container">
  <h2>What-If GPA Analysis</h2>
  <button className="what-if-btn" onClick={toggleModal}>
    Perform What-If Analysis
  </button>
</div>

      {/* Modal for What-If GPA Analysis */}
      {showModal && (
        <div className="modal-overlay">
          <div className="modal-content">
            <h3>What-If GPA Analysis</h3>
            <p>Use this tool to calculate potential GPA changes based on future courses.</p>

            <form>
              <div className="form-group">
                <label htmlFor="currentGPA">Current GPA</label>
                <input type="number" id="currentGPA" placeholder="e.g., 3.5" />
              </div>

              <div className="form-group">
                <label htmlFor="desiredGPA">Desired GPA</label>
                <input type="number" id="desiredGPA" placeholder="e.g., 3.8" />
              </div>

              <div className="form-group">
                <label htmlFor="numCourses">Number of Future Courses</label>
                <input type="number" id="numCourses" placeholder="e.g., 3" />
              </div>

              <div className="form-group">
                <label htmlFor="creditsPerCourse">Credits Per Course</label>
                <input type="number" id="creditsPerCourse" placeholder="e.g., 3" />
              </div>

              <div className="form-group">
                <label htmlFor="averageGrade">Expected Grade for Future Courses</label>
                <input type="text" id="averageGrade" placeholder="e.g., A or B" />
              </div>

              <button type="submit" className="calculate-btn">Calculate GPA</button>
            </form>

            <button className="close-btn" onClick={toggleModal}>
              Close
            </button>
          </div>
        </div>
      )}
    </>
  );
};

export default StudentDashboard;
