import json
import os

DATA_FILE = "data/students.json"


def load_students():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_students(students):
    with open(DATA_FILE, "w") as file:
        json.dump(students, file, indent=4)


def add_student():
    students = load_students()

    student_id = input("Enter student ID: ").strip()
    name = input("Enter student name: ").strip()
    course = input("Enter course: ").strip()

    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists.")
            return

    student = {
        "id": student_id,
        "name": name,
        "course": course
    }

    students.append(student)
    save_students(students)

    print("Student added successfully!")


def view_students():
    students = load_students()

    if not students:
        print("No students found.")
        return

    print("\n----- Student List -----")

    for student in students:
        print(
            f"ID: {student['id']} | "
            f"Name: {student['name']} | "
            f"Course: {student['course']}"
        )


def search_student():
    students = load_students()

    student_id = input("Enter student ID to search: ").strip()

    for student in students:
        if student["id"] == student_id:
            print("\nStudent Found!")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Course:", student["course"])
            return

    print("Student not found.")


def delete_student():
    students = load_students()

    student_id = input("Enter student ID to delete: ").strip()

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            save_students(students)
            print("Student deleted successfully!")
            return

    print("Student not found.")