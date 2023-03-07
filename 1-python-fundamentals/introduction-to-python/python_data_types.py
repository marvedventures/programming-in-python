###########################################################################################################################################
# PYTHON DATA TYPES
###########################################################################################################################################

# 1. NUMERIC

# a. Integer - whole numbers
my_int = 1
print(type(my_int))  # <class 'int'>

# b. Float - decimal numbers
my_float = 10.0
print(type(my_float))  # <class 'float'>

# c. Complex - real & imaginary numbers, ex. a = 10 + 10j
my_complex_number = 10 + 10j
print(type(my_complex_number))  # <class 'complex'>

x = 1j
print(type(x))  # <class 'complex'>
print(x**2 == -1)  # True

###########################################################################################################################################

# 2. SEQUENCE

# a. String
my_string = 'afasfasfsa'
print(type(my_string))  # <class 'str'>

# b. List - sequence of one or more different or similar types
my_list = [1, 2, 'afsfad', 7, 'heaven']
print(type(my_list))  # <class 'list'>

# c. Tuples - similar to list but values are immutable
my_tuple = (1, 2, 'asfafa', 12, True, 'fasfa')
print(type(my_tuple))  # <class 'tuple'>

###########################################################################################################################################

# 3. DICTIONARY
#  - key value pairs
# - As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

my_dict = {
    'name': 'Marvin',
    'last_name': 'Smith',
    'food': ['apple', 'banana', 'corn']
}
print(type(my_dict))  # <class 'dict'>

###########################################################################################################################################

# 4. BOOLEAN
# - True, False
my_bool = True
print(type(my_bool))  # <class 'bool'>

###########################################################################################################################################

# 5. SET
# - unordered, unchangeable*, and unindexed, unique values.
# - Set items are unchangeable, but you can remove items and add new items.
# - the set list is unordered, meaning: the items will appear in a random order.
my_set = {'apple', 'banana', 'corn'}

print(type(my_set))  # <class 'set'>

# Set contains unique values
unique_set = {'apple', 'banana', 'corn', 'corn'}
print(unique_set)  # {'apple', 'banana', 'corn'}

###########################################################################################################################################
