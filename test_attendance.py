import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from validators import is_valid_classes


def test_valid_attendance():
    assert is_valid_classes(20, 18) is True


def test_invalid_attendance():
    assert is_valid_classes(20, 25) is False


def test_zero_classes():
    assert is_valid_classes(0, 0) is False