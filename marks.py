from student import load_students
from validators import is_valid_marks


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def enter_marks():
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

    print("\nEnter marks out of 100:")

    try:
        python_marks = float(input("Python Programming: "))
        mathematics = float(input("Mathematics: "))
        english = float(input("English: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    if not is_valid_marks(python_marks):
        print("Python Programming marks must be between 0 and 100.")
        return

    if not is_valid_marks(mathematics):
        print("Mathematics marks must be between 0 and 100.")
        return

    if not is_valid_marks(english):
        print("English marks must be between 0 and 100.")
        return

    total = python_marks + mathematics + english
    percentage = total / 3
    grade = calculate_grade(percentage)

    selected_student["marks"] = {
        "Python Programming": python_marks,
        "Mathematics": mathematics,
        "English": english
    }

    selected_student["total"] = total
    selected_student["percentage"] = percentage
    selected_student["grade"] = grade

    from student import save_students
    save_students(students)

    print("\nMarks saved successfully!")
    print("Total:", total, "/ 300")
    print("Percentage:", round(percentage, 2), "%")
    print("Grade:", grade)


def view_marks():
    students = load_students()

    student_id = input("Enter student ID: ").strip()

    for student in students:
        if student["id"] == student_id:

            if "marks" not in student:
                print("Marks have not been entered for this student.")
                return

            print("\n===== MARKS DETAILS =====")
            print("Student ID:", student["id"])
            print("Name:", student["name"])

            print("\nPython Programming:",
                  student["marks"]["Python Programming"])

            print("Mathematics:",
                  student["marks"]["Mathematics"])

            print("English:",
                  student["marks"]["English"])

            print("\nTotal:", student["total"], "/ 300")
            print("Percentage:", round(student["percentage"], 2), "%")
            print("Grade:", student["grade"])

            return

    print("Student not found.")