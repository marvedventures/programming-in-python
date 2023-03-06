import pytest
import add_sub


def test_add():
    assert add_sub.add(4, 5) == 9


def test_subtract():
    assert add_sub.subtract(4, 5) == -1

# Run these tests with `python -m pytest 4-modules-packages-libraries-tools/testing-tools/pytest-demo/test_add_sub.py`
# or 'pytest' -> it will run all files of the form test_*.py or *_test.py in the current directory and its subdirectories.
