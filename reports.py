from student import load_students


def generate_report():
    students = load_students()

    if not students:
        print("No students found.")
        return

    print("\n========== STUDENT PERFORMANCE REPORT ==========")

    for student in students:
        print("\n----------------------------------------")
        print("Student ID:", student["id"])
        print("Name:", student["name"])
        print("Course:", student["course"])

        if "marks" in student:
            print("Percentage:", round(student["percentage"], 2), "%")
            print("Grade:", student["grade"])
        else:
            print("Marks: Not entered")

        if "attendance" in student:
            print(
                "Attendance:",
                round(student["attendance"]["percentage"], 2),
                "%"
            )
        else:
            print("Attendance: Not entered")

    print("\n==============================================")