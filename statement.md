# Project Statement: Teacher Portal System

## Problem Statement
In many educational settings, teachers need quick, straightforward access to their assigned students' academic records. However, existing administrative software can often be bloated, complex, or lack simple filtering, forcing teachers to sift through school-wide data. There is a need for a lightweight, fast, and accessible tool that isolates student data based on the specific teacher requesting it, ensuring privacy and ease of use without the overhead of a massive software suite.

## Scope of the Project
This project is a command-line interface (CLI) application built in Python that simulates a school database system. 

**In-Scope:**
* An in-memory data management system utilizing Pandas DataFrames.
* A user authentication system allowing teachers to create accounts and log in securely.
* A personalized data retrieval mechanism that filters and displays only the students assigned to the currently authenticated teacher.
* Prevention of duplicate user accounts during the registration process.

**Out-of-Scope:**
* Persistent database storage (e.g., SQL, MongoDB) – data resets when the script is closed.
* A graphical user interface (GUI) or web front-end.
* Administrative features (like adding new students, editing grades, or deleting accounts from the interface).
* Student-facing or parent-facing portals.

## Target Users
* **Teachers and Educators:** The primary end-users who need a streamlined way to check the names, IDs, and marks of the students assigned to their classes.
* **Educational Administrators:** For demonstrating how role-based data access can be implemented on a small scale.
* **Computer Science Students/Beginners:** Individuals looking for an introductory, real-world application of Python data manipulation using the Pandas library.

## High-Level Features
* **Interactive CLI Dashboard:** A menu-driven interface that is easy to navigate using standard keyboard inputs.
* **Teacher Registration & ID Generation:** A seamless sign-up process that automatically assigns unique numerical IDs to new educators.
* **Secure Authentication Engine:** A login system that matches usernames and passwords against the simulated database.
* **Role-Based Data Filtering:** A dynamic dashboard that cross-references the logged-in teacher's ID with the student database to present a customized, isolated view of relevant student records.