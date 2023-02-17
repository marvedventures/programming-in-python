###########################################################################################################################################
# STRINGS IN PYTHON
###########################################################################################################################################

# - sequence of chars enclosed in single or double quotes

# Single quotes
a = 'Hello'
print(a)

# Double quotes
b = "World"
print(b)

###########################################################################################################################################

# SINGLE LINE STRINGS

a = 'This is a single line string in Python'
print(a)

###########################################################################################################################################

# MULTI-LINE STRINGS

b = 'This is a '\
    'multi-line '\
    'string '\
    'joined in a single-line.'
print(b)

###########################################################################################################################################

# STRING CONCATENATION
# + combines strings

a = 'Hello '
b = 'World!'

print(a + b)  # Hello World!

###########################################################################################################################################

# LEN() FUNCTION ON STRINGS

# The len() function returns the number of items in an object.
# When the object is a string, the len() function returns the number of characters in the string.

# Syntax
# len(object)

# Parameter Values
# object    -> Required. An object. Must be a sequence or a collection

a = 'Hello'
print(len(a))  # 5

###########################################################################################################################################

# ACCESSING STRING CHARACTERS USING INDEX (0-based)

name = 'John Wick'
print(name[0])  # J

###########################################################################################################################################
