###########################################################################################################################################
# WRITING TESTS WITH PYTEST
###########################################################################################################################################

# Installation:
# pip3 install pytest (Mac)
# pip install pytest (Windows)

# assert keyword:
# -> it checks for conditions in your code and expects a Boolean value of true or false. True = test passes, False = test fails

# Running pytest:
# -> python -m pytest file_name
# -> pytest : will run all files of the form test_*.py or *_test.py in the current directory and its subdirectories.

###########################################################################################################################################

# Flags used:
'''
    -v for verbose
    -q quiet mode
    -s allows the print statement inside the functions to be executed
    -x is to flag the tests to stop execution after first failure
    -m is used to mark a specific function
    -k is a flag for searching and running tests with a specific keyword
    --tb is to disable the traceback code of errors
    --maxfail n specifies maximum number of test fails allowed
'''

###########################################################################################################################################

# TIPS:
'''
    - The rule of thumb is that the assert statement looks for a Boolean result. You can use in, not in, is, <, >, other than == to check Boolean values. 
    - You can add multiple assert statements inside a single test function.
'''

###########################################################################################################################################

# ADDITIONAL READING
'''

1. FIXTURES
    -> Fixtures are a type of function that is applied to functions to be tested. These functions must run before that test is executed. The purpose of fixtures is to supply data from multiple sources including URLs and databases to the test before running the test. Fixtures are used in cases where code repeats initialization.
    
    -> Format:
    @pytest.fixture 

2. MARKERS
    -> Markers are used to 'mark' specific functions to be executed by letting users create special names. There are many built-in markers such as xfail, xpass, skip and so on.

    -> Format:
    @pytest.mark.<markername> 

    For example:
    @pytest.mark.alpha 

    Running the specific marked test in the command line can be done with the following command:
    pytest -m <markername> -v 

    Which will be as follows for a marker called alpha.
    pytest -m alpha -v 
    
'''

###########################################################################################################################################
