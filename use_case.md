# Use Case Diagram

```text
                    +-----------------------------+
                    | Student Performance &       |
                    | Attendance Analyzer          |
                    +-----------------------------+
                              |
                    +---------+---------+
                    |                   |
                    v                   v
                [Student]           [Teacher]
                    |                   |
        +-----------+-----------+-------+----------+
        |           |           |                  |
        v           v           v                  v
   Add/View     Manage Marks  Manage           Generate
   Students                  Attendance          Reports
        |           |           |                  |
        +-----------+-----------+------------------+
                            |
                            v
                    Analyze Performance