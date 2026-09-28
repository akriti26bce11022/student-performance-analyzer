# System Architecture

```text
                STUDENT PERFORMANCE
                 & ATTENDANCE
                    ANALYZER
                         |
          +--------------+--------------+
          |              |              |
          v              v              v
   Student Management  Marks        Attendance
          |          Management      Management
          |              |              |
          +--------------+--------------+
                         |
                         v
              Performance Analysis
                         |
                         v
                      Reports
                         |
                         v
                  students.json
                    (JSON Data)