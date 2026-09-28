# System Workflow

```text
START
  |
  v
Main Menu
  |
  +----> Student Management
  |          |
  |          +--> Add Student
  |          +--> View Students
  |          +--> Search Student
  |          +--> Delete Student
  |
  +----> Marks Management
  |          |
  |          +--> Enter Marks
  |          +--> Calculate Percentage
  |          +--> Calculate Grade
  |          +--> View Marks
  |
  +----> Attendance Management
  |          |
  |          +--> Enter Attendance
  |          +--> Calculate Attendance %
  |          +--> View Attendance
  |
  +----> Performance Analysis
  |          |
  |          +--> Read Marks
  |          +--> Read Attendance
  |          +--> Analyze Performance
  |
  +----> Reports
             |
             +--> Generate Student Report
             |
             v
        students.json
             |
             v
            END