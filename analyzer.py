from student import load_students


def analyze_student():
    students = load_students()

    if not students:
        print("No students found.")
        return

    student_id = input("Enter student ID: ").strip()

    for student in students:
        if student["id"] == student_id:

            print("\n===== PERFORMANCE ANALYSIS =====")
            print("Student ID:", student["id"])
            print("Name:", student["name"])

            if "marks" not in student:
                print("Marks have not been entered.")
                return

            if "attendance" not in student:
                print("Attendance has not been entered.")
                return

            percentage = student["percentage"]
            attendance = student["attendance"]["percentage"]

            print("\nAcademic Performance:")
            print("Percentage:", round(percentage, 2), "%")
            print("Grade:", student["grade"])

            print("\nAttendance:")
            print("Attendance:", round(attendance, 2), "%")

            if percentage >= 75 and attendance >= 75:
                performance = "Good"
            elif percentage >= 60 and attendance >= 60:
                performance = "Average"
            else:
                performance = "Needs Improvement"

            print("\nOverall Performance:", performance)

            return

    print("Student not found.")