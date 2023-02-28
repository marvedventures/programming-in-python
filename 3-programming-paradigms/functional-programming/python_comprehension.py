###########################################################################################################################################
# PYTHON COMPREHENSIONS
###########################################################################################################################################

# There are four main types of comprehensions in Python:
# List comprehension
# Dictionary comprehension
# Set comprehension
# Generator comprehension

###########################################################################################################################################

# LIST COMPREHENSIONS
# syntax: [ <expression> for x in <sequence> if <condition>]
# return : list

data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# Ex1: List comprehension: updating the same list
data = [x + 3 for x in data]
# Updating the list:  [5, 6, 8, 10, 14, 16, 20, 22, 26, 32, 34]
print('Updating the list: ', data)

# Ex2: List comprehension: creating a different list with updated values
new_data = [x*2 for x in data]
# Creating new list:  [10, 12, 16, 20, 28, 32, 40, 44, 52, 64, 68]
print('Creating new list: ', new_data)

# Ex3: With an if-condition: Multiples of four:
fourx = [x for x in new_data if x % 4 == 0]
# Divisible by four [12, 16, 20, 28, 32, 40, 44, 52, 64, 68
print('Divisible by four: ', fourx)

# Ex4: Alternatively, we can update the list with the if condition as well
fourxsub = [x-1 for x in new_data if x % 4 == 0]
# Divisible by four minus one:  [11, 15, 19, 27, 31, 39, 43, 51, 63, 67]
print('Divisble by four minus one: ', fourxsub)

# Ex5: Using range function:
nines = [x for x in range(100) if x % 9 == 0]
# Nines:  [0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99]
print('Nines', nines)

###########################################################################################################################################

# list comprehension vs regular for loop vs map()

# NOTE: ALL HAVE THE SAME OUTPUT:
# [5, 6, 8, 10, 14, 16, 20, 22, 26, 32, 34]


# List comprehension:
data_l = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
data_l = [x+3 for x in data_l]
print(data_l)


# Regular for loop:
data_f = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
for idx in range(len(data_f)):
    data_f[idx] = data_f[idx] + 3
print(data_f)


# map()
data_m = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]


def plus_three(x):
    return x+3


print(list(map(plus_three, data_m)))

###########################################################################################################################################

# DICTIONARY COMPREHENSION
# syntax: { key:value for key, value in <sequence> if <condition> }
# return : dict

# Ex1: Using range() function and no input list
using_range = {x: x*2 for x in range(12)}
# Using range():  {0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18, 10: 20, 11: 22}
print('Using range(): ', using_range)

# Lists
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June',
          'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Ex2: Using one input list
num_dict = {x: x**2 for x in number}
# Using one input list to create dict:  {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144}
print('Using one input list to create dict: ', num_dict)

# Ex3: Using two input lists
months_dict = {k: v for (k, v) in zip(number, months)}
# Using two lists:  {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'June', 7: 'July', 8: 'Aug', 9: 'Sept', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
print('Using two lists: ', months_dict)

# NOTE:
# zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.
# If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.

# <zip object at 0x000002F0845AFDC0> ; iterator of tuples
print(zip(number, months))

# use the tuple() function to display a readable version of the result:
# ((1, 'Jan'), (2, 'Feb'), (3, 'Mar'), (4, 'Apr'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'Aug'), (9, 'Sept'), (10, 'Oct'), (11, 'Nov'), (12, 'Dec'))
print(tuple(zip(number, months)))

###########################################################################################################################################

# SET COMPREHENSION
# similar to list compre but uses {}
# syntax : { <expression> for x in <sequence> if <condition> }
# return : set

set_a = {x for x in range(10, 20) if x not in [12, 14, 16]}

# {10, 11, 13, 15, 17, 18, 19}
print('Set in range 10-20(exclusive) but not 12,14,16: ', set_a)

###########################################################################################################################################

# GENERATOR COMPREHENSION
# similar to list but uses () and returns a gen_obj
# more memory efficient as compared to list comprehensions.
# syntax : ( <expression> for x in <sequence> if <condition> )
# return : generator object

data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
gen_obj = (x for x in data)

# <generator object <genexpr> at 0x102a87d60>
print(gen_obj)

# <class 'generator'>
print(type(gen_obj))

# 2 3 5 7 11 13 17 19 23 29 31
for x in gen_obj:
    print(x, end=' ')

###########################################################################################################################################
