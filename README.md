# Student Performance & Attendance Analyzer

## Overview

Student Performance & Attendance Analyzer is a Python-based command-line application designed to manage student information, marks, attendance, performance analysis, and reports.

The project helps organize student academic data and provides a simple way to analyze overall performance.

## Features

- Add, view, search, and delete students
- Enter and view student marks
- Calculate percentage and grades
- Enter and view attendance
- Calculate attendance percentage
- Analyze overall student performance
- Generate student performance reports
- Input validation
- Error handling
- Automated testing using pytest
- JSON-based data storage

## Technologies Used

- Python
- JSON
- pytest
- VS Code
- Git and GitHub

## Project Structure

```text
student-performance-analyzer/
├── data/
│   └── students.json
├── tests/
│   ├── test_student.py
│   ├── test_marks.py
│   └── test_attendance.py
├── analyzer.py
├── attendance.py
├── main.py
├── marks.py
├── reports.py
├── student.py
├── validators.py
├── requirements.txt
└── README.md