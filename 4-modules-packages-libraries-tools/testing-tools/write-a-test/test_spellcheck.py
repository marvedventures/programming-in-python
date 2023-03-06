''' 
Import statements: 
    1. Import pytest and spellcheck modules
'''
import pytest
import spellcheck

# String variables to be tested
alpha = 'Checking the length & structure of the sentence.'
beta = 'This sentence should fail the test'


# Do not delete this function. You may change the value assigned to input to test different inputs to your test functions.
@pytest.fixture
def input_value():
    input = alpha
    return input


# First test function test_length()
def test_length(input_value):
    ''' 
    Tests whether a string has fewer than 10 words and fewer than 50 chars.
    '''
    assert spellcheck.word_count(input_value) < 10
    assert spellcheck.char_count(input_value) < 50


# Second test function test_struc()
def test_struc(input_value):
    ''' 
    Tests whether a string begins with a capital letter and ends with a period.
    '''
    assert spellcheck.first_char(input_value).isupper()
    assert spellcheck.last_char(input_value) == '.'


# Run these tests with `python -m pytest 4-modules-packages-libraries-tools/testing-tools/write-a-test/test_spellcheck.py`
# or 'pytest' -> it will run all files of the form test_*.py or *_test.py in the current directory and its subdirectories.
