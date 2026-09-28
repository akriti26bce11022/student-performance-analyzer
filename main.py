from student import (
    add_student,
    view_students,
    search_student,
    delete_student
)

from marks import enter_marks, view_marks
from attendance import enter_attendance, view_attendance
from analyzer import analyze_student
from reports import generate_report
def student_menu():
    while True:
        print("\n===== STUDENT MANAGEMENT =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")


def main():
    while True:
        print("\n======================================")
        print(" STUDENT PERFORMANCE & ATTENDANCE")
        print("            ANALYZER")
        print("======================================")

        print("\n1. Student Management")
        print("2. Marks Management")
        print("3. Attendance Management")
        print("4. Performance Analysis")
        print("5. Reports")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_menu()

        elif choice == "2":
            while True:
                print("\n===== MARKS MANAGEMENT =====")
                print("1. Enter Marks")
                print("2. View Marks")
                print("3. Back to Main Menu")

                marks_choice = input("Enter your choice: ")

                if marks_choice == "1":
                    enter_marks()

                elif marks_choice == "2":
                    view_marks()

                elif marks_choice == "3":
                    break

                else:
                    print("Invalid choice. Please try again.")

        elif choice == "3":
            while True:
                print("\n===== ATTENDANCE MANAGEMENT =====")
                print("1. Enter Attendance")
                print("2. View Attendance")
                print("3. Back to Main Menu")

                attendance_choice = input("Enter your choice: ")

                if attendance_choice == "1":
                    enter_attendance()

                elif attendance_choice == "2":
                    view_attendance()

                elif attendance_choice == "3":
                    break

                else:
                    print("Invalid choice. Please try again.")

        elif choice == "4":
            analyze_student()

        elif choice == "5":
            generate_report()

        elif choice == "6":
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()