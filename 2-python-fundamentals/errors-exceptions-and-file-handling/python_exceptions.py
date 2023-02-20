###########################################################################################################################################
# PYTHON EXCEPTIONS
###########################################################################################################################################

# PYTHON ERRORS
# 1. Syntax Errors
# - human errors, mispelling, typos
# - SyntaxError, IndentationError, etc

# 2. Exception Errors
# - known errors that need to be handled
# - ZeroDivisionError, etc

def divide_by(a, b):
    return a / b

# divide_by(4, 0)  # ZeroDivisionError: division by zero

###########################################################################################################################################

# EXCEPTION HANDLING - try/except


try:
    ans = divide_by(4, 0)
except:
    print('Something went wrong!')  # Something went wrong!


# Generic Exceptions
try:
    ans = divide_by(4, 0)
except Exception as e:
    print('Something went wrong!', e)  # Something went wrong! division by zero
    print(e.__class__)  # <class 'ZeroDivisionError'>


# Specific Exceptions
try:
    ans = divide_by(4, 0)
except ZeroDivisionError as e:
    print(e, 'We cannot divide it by zero.')
    # division by zero We cannot divide it by zero.


# Chaining Exceptions
try:
    ans = divide_by(4, 0)
except ZeroDivisionError as e:
    print(e, 'We cannot divide it by zero.')
except Exception as e:
    print(e, 'Something went wrong!')


###########################################################################################################################################
