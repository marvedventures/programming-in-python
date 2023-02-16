# TYPE CASTING/CONVERSION

# Typecasting is the process of converting one data type to another
# Can be Implicit / Explicit

###########################################################################################################################################

# IMPLICIT - automatic

# INT TO FLOAT

my_int = 10
my_float = 20.2

print(my_int + my_float)  # 30.2

###########################################################################################################################################

# EXPLICIT - manual

# 1. int() - argument must be a string, a bytes-like object or a real number

print(int('12345'))  # 12345
print(int(20.234))  # 20
print(int(False))  # 0

###########################################################################################################################################

# 2. float() - argument must be a string, a bytes-like object or a real number

print(float('30'))  # 30.0
print(float(20))  # 20.0
print(float(True))  # 1.0

###########################################################################################################################################

# 3. complex() - argument must be a string, a bytes-like object or a real number

print(complex('40'))  # (40+0j)
print(complex(15))  # (15+0j)
print(complex(True))  # (1+0j)

###########################################################################################################################################

# 4. str()  - returns the string representation of a given object

print(str(1))  # '1'
print(str(False))  # 'False'
print(str({1, 2, 3, 4}))  # '{1, 2, 3,4 }'

###########################################################################################################################################

# 5. list() - argument must be an iterable (string, tuple, set, dict(but only 'keys' are stored in a list))
print(list('Marvin'))  # ['M', 'a', 'r', 'v', 'i', 'n']
print(list(('apple', 'banana', 'corn')))  # ['apple', 'banana', 'corn']

print(list({'apple', 'banana', 'corn'}))
# ['apple', 'banana', 'corn']  -> position can be in random order

print(list({'name': 'Marvin', 'gender': 'Male'}))  # ['name', 'gender']

###########################################################################################################################################

# 6. tuple() - argument must be an iterable (string, tuple, set, dict(but only 'keys' are stored in a list))
print(tuple('Marvin'))  # ('M', 'a', 'r', 'v', 'i', 'n')
print(tuple(['M', 7, 8, 'j', True]))  # ('M', 7, 8, 'j', True)

# ('apple', 'banana' 'corn') -> position can be in random order
print(tuple({'apple', 'banana', 'corn'}))
print(tuple({'name': 'Marvin', 'gender': 'Male'}))  # ('name', 'gender')

###########################################################################################################################################

# 7. set() - argument must be an iterable (string, tuple, set, dict(but only 'keys' are stored in a list))
# NOTE: the set list is unordered, meaning: the items will appear in a random order.

print(set('Marvin'))  # ('M', 'a', 'r', 'v', 'i', 'n')
print(set(['M', 7, 8, 'j', True]))  # ('M', 7, 8, 'j', True)

# ('apple', 'banana' 'corn') -> position can be in random order
print(set({'apple', 'banana', 'corn'}))
print(set({'name': 'Marvin', 'gender': 'Male'}))  # ('name', 'gender')

###########################################################################################################################################

# 8. bool()
# False - Falsy values (empty sequences (lists, tuples, strings, dictionaries, sets), zero in every numeric type, None , and False)
# True - if argument is any number (besides 0), True or a string, not empty collection

print(bool(0))  # False
print(bool([]))  # False
print(bool({}))  # False

print(bool(1))  # True
print(bool('0'))  # True
print(bool([1, 2, 3]))  # True

###########################################################################################################################################

# 9. dict() - argument of the form kwarg=value

print(dict(x=5, y=0))  # {'x': 5, 'y': 0}
print('my_dict =', dict(x=5, y=0))  # my_dict = {'x': 5, 'y': 0}

###########################################################################################################################################

# OTHER TYPECASTING FUNCTIONS

# 1. ord() - returns an integer representing the Unicode character.

unicode_char = 'P'
my_ord = ord(unicode_char)
print(my_ord)  # 80

# NOTE: ord() function is the inverse of the Python chr() function.


# 2. hex() -  converts an integer number to the corresponding hexadecimal string

number = 423
my_hex = hex(number)
print(my_hex)  # 0x1a7

# 3. oct() - converts an integer to a string representing an octal number

number = 432
my_oct = oct(number)
print(my_oct)  # 0o660

###########################################################################################################################################
