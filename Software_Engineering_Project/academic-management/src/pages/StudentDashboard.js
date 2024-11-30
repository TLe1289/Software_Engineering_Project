import React, { useState } from 'react';
import './StudentDashboard.css'; // Import dashboard-specific styles

const StudentDashboard = () => {
  const [showModal, setShowModal] = useState(false);
  const [selectedScenario, setSelectedScenario] = useState(null);
  const [result, setResult] = useState(null);

  const toggleModal = () => {
    setShowModal(!showModal);
    setSelectedScenario(null); // Reset scenario selection when modal is closed
    setResult(null); // Clear results when modal is closed
  };

  const handleScenarioSelect = (scenario) => {
    setSelectedScenario(scenario);
    setResult(null); // Clear results for new selection
  };

  const handleScenario1Submit = async (event) => {
    event.preventDefault();

    // Collect form values
    const currentGPA = event.target.currentGPA.value;
    const numCoursesTaken = event.target.numCoursesTaken.value;
    const numCourses = event.target.numCourses.value;
    const creditsPerCourse = event.target.creditsPerCourse.value;
    const averageGrade = event.target.averageGrade.value;

    try {
      // Send POST request to the backend
      const response = await fetch('http://localhost:8080/api/what-if/scenario1', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          currentGPA: parseFloat(currentGPA),
          numCoursesTaken: parseInt(numCoursesTaken),
          numCourses: parseInt(numCourses),
          creditsPerCourse: parseInt(creditsPerCourse),
          averageGrade,
        }),
      });

      const data = await response.json();
      setResult(`New GPA: ${data.newGPA}`);
    } catch (error) {
      setResult('Error calculating GPA. Please try again.');
    }
  };

  const handleScenario2Submit = async (event) => {
    event.preventDefault();

    // Collect form values
    const currentGPA = event.target.currentGPA.value;
    const numCoursesTaken = event.target.numCoursesTaken.value;
    const desiredGPA = event.target.desiredGPA.value;
    const creditsPerCourse = event.target.creditsPerCourse.value;
    const averageGrade = event.target.averageGrade.value;

    try {
      // Send POST request to the backend
      const response = await fetch('http://localhost:8080/api/what-if/scenario2', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          currentGPA: parseFloat(currentGPA),
          numCoursesTaken: parseInt(numCoursesTaken),
          desiredGPA: parseFloat(desiredGPA),
          creditsPerCourse: parseInt(creditsPerCourse),
          averageGrade,
        }),
      });

      const data = await response.json();
      setResult(`Number of Courses Required: ${data.numCoursesRequired}`);
    } catch (error) {
      setResult('Error calculating courses. Please try again.');
    }
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

      {/* Section 2: What-If GPA Analysis */}
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
            {!selectedScenario && (
              <>
                <p>Select a scenario for the analysis:</p>
                <div style={{ display: 'flex', flexDirection: 'column', gap: '5px' }}>
                  <button
                    className="scenario-btn"
                    onClick={() => handleScenarioSelect(1)}
                  >
                    Impact of Future Courses
                  </button>
                  <button
                    className="scenario-btn"
                    onClick={() => handleScenarioSelect(2)}
                  >
                    Path to Desired GPA
                  </button>
                </div>
              </>
            )}

            {selectedScenario === 1 && (
              <form onSubmit={handleScenario1Submit}>
                <h4>Impact of Future Courses</h4>
                <div className="form-group">
                  <label htmlFor="currentGPA">Current GPA</label>
                  <input type="number" id="currentGPA" name="currentGPA" placeholder="e.g., 3.5" required />
                </div>
                <div className="form-group">
                  <label htmlFor="numCoursesTaken">Number of Courses Taken</label>
                  <input type="number" id="numCoursesTaken" name="numCoursesTaken" placeholder="e.g., 15" required />
                </div>
                <div className="form-group">
                  <label htmlFor="numCourses">Number of Future Courses</label>
                  <input type="number" id="numCourses" name="numCourses" placeholder="e.g., 3" required />
                </div>
                <div className="form-group">
                  <label htmlFor="creditsPerCourse">Credits Per Course</label>
                  <input type="number" id="creditsPerCourse" name="creditsPerCourse" placeholder="e.g., 3" required />
                </div>
                <div className="form-group">
                  <label htmlFor="averageGrade">Expected Grade for Future Courses</label>
                  <input type="text" id="averageGrade" name="averageGrade" placeholder="e.g., A or B" required />
                </div>
                <button type="submit" className="calculate-btn">Calculate GPA</button>
              </form>
            )}

            {selectedScenario === 2 && (
              <form onSubmit={handleScenario2Submit}>
                <h4>Path to Desired GPA</h4>
                <div className="form-group">
                  <label htmlFor="currentGPA">Current GPA</label>
                  <input type="number" id="currentGPA" name="currentGPA" placeholder="e.g., 3.5" required />
                </div>
                <div className="form-group">
                  <label htmlFor="numCoursesTaken">Number of Courses Taken</label>
                  <input type="number" id="numCoursesTaken" name="numCoursesTaken" placeholder="e.g., 15" required />
                </div>
                <div className="form-group">
                  <label htmlFor="desiredGPA">Desired GPA</label>
                  <input type="number" id="desiredGPA" name="desiredGPA" placeholder="e.g., 3.8" required />
                </div>
                <div className="form-group">
                  <label htmlFor="creditsPerCourse">Credits Per Course</label>
                  <input type="number" id="creditsPerCourse" name="creditsPerCourse" placeholder="e.g., 3" required />
                </div>
                <div className="form-group">
                  <label htmlFor="averageGrade">Expected Grade for Future Courses</label>
                  <input type="text" id="averageGrade" name="averageGrade" placeholder="e.g., A or B" required />
                </div>
                <button type="submit" className="calculate-btn">Calculate Courses</button>
              </form>
            )}

            {result && (
              <div className="result">
                <h4>Result:</h4>
                <p>{result}</p>
              </div>
            )}

            <button className="close-btn" onClick={toggleModal}>Close</button>
          </div>
        </div>
      )}
    </>
  );
};

export default StudentDashboard;
