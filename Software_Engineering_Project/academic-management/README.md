
# Academic Management System - Frontend (React)

This is the frontend for the Academic Management System project, built using React.js. The system provides different user interfaces for students, instructors, staff, and advisors, allowing them to manage or view academic data such as student enrollments, course details, and GPA analysis.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Available Scripts](#available-scripts)
- [Project Structure](#project-structure)
- [Running the App](#running-the-app)
- [Features](#features)
- [License](#license)

## Prerequisites
Before running this project, ensure you have the following tools installed:
- Node.js (version 16)
- npm (comes with Node.js)
- Git

## Installation

### Step 1: Clone the repository
To get started, clone the repository from GitHub:

```bash
git clone https://github.com/TLe1289/Software_Engineering_Project.git
```

### Step 2: Navigate into the project directory
```bash
cd academic-management-system
```

### Step 3: Install the dependencies
Install the required packages using npm:

```bash
npm install
```

This will install all the dependencies listed in the `package.json` file, including React and related libraries.

## Available Scripts
In the project directory, you can run the following commands:

- `npm start`  
  Runs the app in development mode. Open [http://localhost:3000](http://localhost:3000) to view it in your browser. The page will automatically reload if you make edits. You will also see any linting errors in the console.

## Project Structure

```
├── public
│   ├── index.html        # Main HTML template
│   ├── manifest.json     # PWA settings (optional)
├── src
│   ├── components        # Reusable React components
│   ├── pages             # Individual pages for different user types
│   │   ├── Login.js / css      # Login page component
│   │   ├── StudentDashboard.js /css    # Student dashboard
│   │   ├── InstructorDashboard.js / css    # Instructor dashboard
│   │   ├── AdvisorDashboard.js / css     # Advisor dashboard
│   │   └── ...
│   ├── App.js            # Main React app component
│   ├── index.js          # Entry point for React
│   ├── index.css         # Global styles
│   └── ...
├── package.json          # Project metadata and dependencies
└── README.md             # Instructions for running the project
```

## Running the App

Once the dependencies are installed, you can run the app with the following steps:

### Step 1: Start the development server
```bash
npm start
```

This will start the development server, and you can view the app at [http://localhost:3000](http://localhost:3000).

### Step 2: Interact with the App
You will be presented with a Login page where you can choose a role (Student, Instructor, Advisor, etc.) from the dropdown and navigate to the respective dashboard.  
Each dashboard (e.g., `StudentDashboard`, `InstructorDashboard`, `AdvisorDashboard`) will display user-specific information and actions based on the role.

### Step 3: Make changes or explore
You can modify the source files in the `src` directory to customize the behavior of the app. Any changes you make will reflect automatically after saving.

## Features
- **Login Page**: Allows users to select a role and log in to the system.
- **Student Dashboard**: View GPA, course enrollments, and perform "What-If" GPA analysis.
- **Instructor Dashboard**: View course details.
- **Advisor Dashboard**: Manage student enrollments, and add/drop courses.
