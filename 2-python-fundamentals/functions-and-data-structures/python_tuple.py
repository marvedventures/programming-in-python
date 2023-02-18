###########################################################################################################################################
# PYTHON TUPLE
###########################################################################################################################################

# TUPLE
# collection which is ordered and unchangeable.
# can accept any mix of data types.

# immutable

# can be written with or without parenthesis ()
# for best practice, write with parenthesis()

my_tuple1 = 'apple', 'banana', 'cherry'
my_tuple2 = ('apple', 'cherry',  'banana', 'cherry', 'cherry')
my_tuple3 = (1, 'string', 2.00, True)


print(type(my_tuple1))  # <class 'tuple'>
print(type(my_tuple2))  # <class 'tuple'>


print(my_tuple1.index('apple'))  # 0
print(my_tuple2.count('cherry'))  # 3

###########################################################################################################################################

# PYTHON TUPLE BUILT- IN METHODS

# count()	- returns the number of times a specified value occurs in a tuple
# index()	- searches the tuple for a specified value and returns the position of where it was found
