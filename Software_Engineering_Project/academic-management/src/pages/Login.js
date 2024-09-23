import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './Login.css';  // Import Login-specific styles

const Login = () => {
  const [role, setRole] = useState('');
  const navigate = useNavigate();

  const handleRoleSelect = (e) => {
    setRole(e.target.value);
  };

  const handleLogin = (e) => {
    e.preventDefault();

    if (role === 'student') {
      navigate('/student-dashboard');
    } else if (role === 'staff') {
      navigate('/staff-dashboard');
    } else if (role === 'instructor') {
      navigate('/instructor-dashboard');
    } else if (role === 'advisor') {
      navigate('/advisor-dashboard');
    } else {
      alert('Please select a role');
    }
  };

  return (
    <div className="login-card">
      <h2 className="login-title">Sign in</h2>
      <p className="login-subtitle">Please enter your login details</p>

      <input
        className="login-input"
        type="username"
        placeholder="Username"
        required
      />

      <input
        className="login-input"
        type="password"
        placeholder="Password"
        required
      />

      <select
        className="login-select"
        value={role}
        onChange={handleRoleSelect}
        required
      >
        <option value="" disabled>
          Select Role
        </option>
        <option value="student">Student</option>
        <option value="staff">Staff</option>
        <option value="instructor">Instructor</option>
        <option value="advisor">Advisor</option>
      </select>

      <button className="login-btn" onClick={handleLogin}>
        Login
      </button>
    </div>
  );
};

export default Login;
