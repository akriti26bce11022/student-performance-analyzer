from student import load_students, save_students
from validators import is_valid_classes


def enter_attendance():
    students = load_students()

    if not students:
        print("No students found. Please add a student first.")
        return

    student_id = input("Enter student ID: ").strip()

    selected_student = None

    for student in students:
        if student["id"] == student_id:
            selected_student = student
            break

    if selected_student is None:
        print("Student not found.")
        return

    try:
        total_classes = int(input("Enter total number of classes: "))
        attended_classes = int(input("Enter number of classes attended: "))
    except ValueError:
        print("Invalid input. Please enter whole numbers only.")
        return

    if not is_valid_classes(total_classes, attended_classes):
        print("Invalid attendance values.")
        print("Attended classes cannot be greater than total classes.")
        return

    if attended_classes > total_classes:
        print("Attended classes cannot be greater than total classes.")
        return

    if total_classes <= 0:
        print("Total classes must be greater than 0.")
        return

    attendance_percentage = (
        attended_classes / total_classes
    ) * 100

    selected_student["attendance"] = {
        "total_classes": total_classes,
        "attended_classes": attended_classes,
        "percentage": attendance_percentage
    }

    save_students(students)

    print("\nAttendance saved successfully!")
    print("Attendance:", round(attendance_percentage, 2), "%")


def view_attendance():
    students = load_students()

    student_id = input("Enter student ID: ").strip()

    for student in students:
        if student["id"] == student_id:

            if "attendance" not in student:
                print("Attendance has not been entered for this student.")
                return

            print("\n===== ATTENDANCE DETAILS =====")
            print("Student ID:", student["id"])
            print("Name:", student["name"])
            print(
                "Total Classes:",
                student["attendance"]["total_classes"]
            )
            print(
                "Attended Classes:",
                student["attendance"]["attended_classes"]
            )
            print(
                "Attendance:",
                round(student["attendance"]["percentage"], 2),
                "%"
            )

            return

    print("Student not found.")