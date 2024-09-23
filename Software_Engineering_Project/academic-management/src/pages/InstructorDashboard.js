import React from 'react';
import './InstructorDashboard.css'; // Import instructor-specific styles

const InstructorDashboard = () => {
  return (
    <>
      {/* Section 1: Instructor Information */}
      <div className="container">
        <h2>Instructor Information</h2>
        <p><strong>Instructor ID:</strong> I987654</p>
        <p><strong>Phone Number:</strong> +123456789</p>
        <p><strong>Department ID:</strong> D001</p>
        <p><strong>Department Phone:</strong> 6114</p>
        <p><strong>Hired Semester:</strong> Fall 2020</p>
        <p><strong>Department Building:</strong> G</p>
        <p><strong>Department Office:</strong> 233</p>
      </div>

      {/* Section 2: Courses Taught */}
      <div className="container">
        <h2>Courses</h2>
        <div className="table-wrapper">
          <table className="courses-table">
            <thead>
              <tr>
                <th>Course Prefix</th>
                <th>Course Number</th>
                <th>Credit</th>
                <th>Semester</th>
                <th>Year Taught</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>CS</td>
                <td>201</td>
                <td>3</td>
                <td>Fall</td>
                <td>2022</td>
              </tr>
              <tr>
                <td>CS</td>
                <td>301</td>
                <td>4</td>
                <td>Spring</td>
                <td>2023</td>
              </tr>
              {/* Add more rows as needed */}
            </tbody>
          </table>
        </div>
      </div>

      {/* Section 3: Students of the Instructor */}
      <div className="container">
        <h2>Current Students</h2>
        <div className="table-wrapper">
          <table className="students-table">
            <thead>
              <tr>
                <th>Student Name</th>
                <th>Semester</th>
                <th>Course Number</th>
                <th>Grade</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>John Doe</td>
                <td>Fall 2022</td>
                <td>CS201</td>
                <td>A</td>
              </tr>
              <tr>
                <td>Jane Smith</td>
                <td>Spring 2023</td>
                <td>CS301</td>
                <td>B</td>
              </tr>
              {/* Add more rows as needed */}
            </tbody>
          </table>
        </div>
      </div>
    </>
  );
};

export default InstructorDashboard;
