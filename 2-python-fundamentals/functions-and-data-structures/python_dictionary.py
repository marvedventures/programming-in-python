###########################################################################################################################################
# PYTHON DICTIONARY
###########################################################################################################################################

# DICTIONARY

# Dictionary items are ordered, changeable, and does not allow duplicates.
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
# The values in dictionary items can be of any data type:

# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# If key is duplicated, it will overwritten the previous key


my_dict = {1: 'Test', 'name': 'Jim'}

print(my_dict)  # {1: 'Test', 'name': 'Jim'}

# does not allow duplicates, previous item on key 1 will be overwritten
my_dict = {1: 'Test',
           'name': 'Jim',
           1: 'Test is overwritten'}

print(my_dict)
# {1: 'Previous item on key 1 will be overwritten', 'name': 'Jim'}

###########################################################################################################################################

# ACCESSING VALUE IN DICTIONARY

# Bracket Notation
# - can access the items of a dictionary by referring to its key name, inside square brackets

this_dict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}

print(this_dict['brand'])  # 'Ford'

###########################################################################################################################################

# ADDING AND UPDATING NEW VALUE IN DICTIONARY

# ADDING NEW VALUE IS THE SAME AS UPDATING NEW VALUE
# THERE'S AN EXISTING KEY -> UPDATE
# NO EXISTING KEY -> ADD

this_dict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}

# ADDING -> no existing key
this_dict['Owner'] = 'James Bond'

print(this_dict)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'Owner': 'James Bond'}

# UPDATING -> overriding previous key
this_dict['year'] = 2011

print(this_dict)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 2011, 'Owner': 'James Bond'}

###########################################################################################################################################

# DELETING A VALUE IN DICTIONARY

del this_dict['brand']

print(this_dict)
# {'model': 'Mustang', 'year': 2011, 'Owner': 'James Bond'}

###########################################################################################################################################

# ITERATING THROUGH A DICTIONARY

this_dict = {
    1: 'Test',
    'name': 'Jim'
}


# KEYS ONLY
for key in this_dict:
    print(key)
    # 1
    # 'name'

# KEY : VALUES

for key, value in this_dict.items():
    print(str(key) + ' : ' + value)
    # 1 : Test
    # name : Jim

###########################################################################################################################################
