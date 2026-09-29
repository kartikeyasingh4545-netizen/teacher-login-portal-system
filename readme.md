# Teacher Portal System

## Overview of the Project
The Teacher Portal System is a lightweight, command-line Python application designed to simulate a school database interface. It allows educators to create accounts, securely log in, and view a personalized dashboard displaying the academic records of the students assigned specifically to them. The system uses Pandas DataFrames to simulate an in-memory database for quick and efficient data handling.

## Features
*   **User Registration:** Teachers can sign up and create a new account, automatically generating a unique Teacher ID (`tid`).
*   **Secure Login System:** Validates usernames and passwords against the existing teacher database before granting access.
*   **Duplicate Username Prevention:** Ensures that all teacher usernames in the system are unique.
*   **Personalized Student Dashboard:** Upon successful login, the system filters the student database and displays only the students assigned to the logged-in teacher.
*   **Interactive CLI:** Easy-to-use, menu-driven command-line interface.

## Technologies/Tools Used
*   **Python 3:** The core programming language used to build the application.
*   **Pandas:** A powerful data manipulation library used here to act as an in-memory database (DataFrames) for managing teacher and student records.

## Steps to Install & Run the Project
1. **Prerequisites:** Ensure you have Python 3 installed on your system. You can download it from [python.org](https://www.python.org/).
2. **Install Pandas:** Since the project relies on the Pandas library, you need to install it via pip. Open your terminal or command prompt and run:
   ```bash
   pip install pandas
   ```
3. **Download the Script:** Save the provided python code into a file named `teacher_portal.py`.
4. **Run the Application:** Navigate to the directory where you saved `teacher_portal.py` in your terminal and execute the following command:
   ```bash
   python teacher_portal.py
   ```

## Instructions for Testing
To ensure the application is working correctly, you can perform the following test cases in the terminal once the script is running:

**Test 1: Pre-existing Login & Data Retrieval**
1. Select option `1` (Login).
2. Enter Username: `dheresh soni`
3. Enter Password: `12345`
4. *Expected Result:* Login successful. The dashboard should display three students: anurag (85), hanshal (92), and saurabh (78).

**Test 2: Account Creation**
1. Select option `2` (Create New Account).
2. Enter a new Username (e.g., `new teacher`).
3. Enter a Password (e.g., `pass123`).
4. *Expected Result:* Account creation successful, and the system assigns a new Teacher ID (ID: 3).

**Test 3: Duplicate Username Handling**
1. Select option `2` (Create New Account).
2. Enter an existing Username (e.g., `hemant kumar`).
3. *Expected Result:* The system should reject the registration and state that the username already exists.

**Test 4: Invalid Login Handling**
1. Select option `1` (Login).
2. Enter an invalid Username or Password.
3. *Expected Result:* The system should display "Invalid username or password. Access Denied."

**Test 5: Exit System**
1. Select option `3` (Exit).
2. *Expected Result:* The program terminates gracefully with a goodbye message.