import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from student import load_students


def test_load_students():
    students = load_students()
    assert isinstance(students, list)


def test_student_data_structure():
    students = load_students()

    if students:
        student = students[0]

        assert "id" in student
        assert "name" in student
        assert "course" in student