import findstring
import pytest


# 1. create test first
def test_ispresent():
    assert findstring.is_present('Al')


# 3.
# run test with `python -m pytest 4-modules-packages-libraries-tools/testing-tools/tdd-demo/test_findstring.py
# or 'pytest' -> it will run all files of the form test_*.py or *_test.py in the current directory and its subdirectories.
