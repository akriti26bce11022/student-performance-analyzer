import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from marks import calculate_grade


def test_grade_a_plus():
    assert calculate_grade(95) == "A+"


def test_grade_a():
    assert calculate_grade(85) == "A"


def test_grade_f():
    assert calculate_grade(40) == "F"