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

# Exercise: Exceptions in Python

# Your task in this exercise is to add code to trap exceptions and handle them in a more user-friendly way.

# 1. IndexError
# The below code has one problem. It is trying to locate an item from the list that does not exist.
# Running the code will throw the IndexError.
# Add exception handling to stop the error from being thrown and return a more user-friendly message such as "Item does not exist in the list".

# Starter code:
# items = [1,2,3,4,5]
# item = items[6]
# print(item)

# Answer:
items = [1, 2, 3, 4, 5]
try:
    item = items[6]
    print(item)
except:
    print('Item does not exist in the list.')

###########################################################################################################################################

# 2.ZeroDivisionError
# In math there are rules about dividing by zero.
# The below code is trying to do just that and will throw a ZeroDivisionError.
# Add exception handling to return back 0 instead of allowing the error to be thrown.


# Starter code
# def divide_by(a, b):
#     return a / b
# ans = divide_by(40, 0)
# print(ans)

# Answer:
def divide_by(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return 0
    except Exception as e:
        print(e, 'Something went wrong!')


ans = divide_by(40, 0)
print(ans)

###########################################################################################################################################

# 3. FileNotFoundError
# The code below is looking for a file that does not exist.
# Add exception handling to catch this error and return the following "The file could not be found".

# Starter code
# with open('file_does_not_exist.txt', 'r') as file:
#     print(file.read())

# Answer:
try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except:
    print('The file cound not be found')

###########################################################################################################################################
