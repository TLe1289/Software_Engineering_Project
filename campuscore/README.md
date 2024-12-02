# Campus Core

## Quick Start Guide

This guide will help you set up and run the application on macOS. Follow the steps below to install the prerequisites and get started.

### Prerequisites

Before you begin, ensure you have the following installed:

- [Homebrew](https://brew.sh/): Package manager for macOS
- [Node.js](https://nodejs.org/): JavaScript runtime
- [Python 3](https://www.python.org/): Programming language

#### Install Prerequisites Using Homebrew

Open your terminal and run the following commands to install the necessary tools:

1. **Install Homebrew** (if not already installed):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install Python 3**:
   ```bash
   brew install python
   ```

3. **Install Node.js**:
   ```bash
   brew install node
   ```

### Build and Run the Application

Once you have the prerequisites installed, you can build and run the application using the provided Makefile.

1. **Build the Application**:
   ```bash
   make build
   ```
   This command will create a Python virtual environment, install the necessary Python packages, and build the frontend assets using npm.

2. **Collect Static Files**:
   ```bash
   make collectstatic
   ```
   This command will collect static files for the application.

3. **Create and Apply Migrations**:
   ```bash
   make migrations
   ```
   This command will create and apply database migrations.

4. **Flush the Database**:
   ```bash
   make flush
   ```
   This command will flush the database.

5. **Load Fixtures**:
   ```bash
   make loaddata
   ```
   This command will load initial data fixtures into the database.

6. **Run the Server**:
   ```bash
   make run
   ```
   This command will start the development server which can be accessed at http://127.0.0.1:8000/ui/login/

7. **Format Code**:
   ```bash
   make format
   ```
   This command will format the code using `black` and `isort`.

### Additional Information

- For more detailed information on each command, refer to the `Makefile` in the project directory.

Enjoy developing with this setup!
