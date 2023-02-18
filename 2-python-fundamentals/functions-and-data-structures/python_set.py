###########################################################################################################################################
# PYTHON SET
###########################################################################################################################################

# SET
# - collection which is unordered, unchangeable*, and unindexed.
# - written with curly brackets.
# *set items are unchangeable, but you can remove items and add new items.

set_a = {'apple', 'banana', 'orange', 'lemon', 'corn'}
set_b = {'apple', 'banana', 'papaya', 'mango', 'watermelon'}

print(set_a)

###########################################################################################################################################

# ADD
set_a.add('grapes')
# NOTE: ORDER MAY CHANGE {'apple', 'corn', 'lemon', 'orange', 'grapes', 'banana'}
print(set_a)

###########################################################################################################################################

# REMOVE
set_a.remove('orange')
print(set_a)

# DISCARD
set_a.discard('orange')
print(set_a)

###########################################################################################################################################

# MATHEMATICAL OPERATIONS

set_a = {'apple', 'banana', 'orange', 'lemon', 'corn'}
set_b = {'apple', 'banana', 'papaya', 'mango', 'watermelon'}

# 1. UNION
# - union of sets (no duplicates)
# union() or |

print(set_a.union(set_b))
# {'watermelon', 'apple', 'mango', 'orange', 'corn', 'papaya', 'lemon', 'banana'}

print(set_a | set_b)
# {'watermelon', 'apple', 'mango', 'orange', 'corn', 'papaya', 'lemon', 'banana'}

###########################################################################################################################################

# 2. INTERSECTION
# intersection of two sets(duplicates)
# intersection() or &

print(set_a.intersection(set_b))
# {'banana', 'apple'}

print(set_a & set_b)
# {'banana', 'apple'}

###########################################################################################################################################

# 3. DIFFERENCE
# - difference between two sets (only inside a or only inside b)
# - difference() or -

# will print elements only inside a
print(set_a.difference(set_b))  # {'lemon', 'orange', 'corn'}

# will print elements only inside b
print(set_b - set_a)  # {'watermelon', 'mango', 'papaya'}

###########################################################################################################################################

# 4. SYMMETRIC DIFFERENCE
# - returns a set with the symmetric differences of two sets
# - symmetric_difference() or ^

print(set_a.symmetric_difference(set_b))
# {'papaya', 'lemon', 'orange', 'corn', 'mango', 'watermelon'}

print(set_a ^ set_b)
# {'papaya', 'lemon', 'orange', 'corn', 'mango', 'watermelon'}

###########################################################################################################################################

# PYTHON SET BUILT-IN METHODS

# add()	                            - adds an element to the set
# clear()	                        - removes all the elements from the set
# copy()	                        - returns a copy of the set
# difference()	                    - returns a set containing the difference between two or more sets
# difference_update()	            - removes the items in this set that are also included in another, specified set
# discard()	                        - remove the specified item
# intersection()	                - returns a set, that is the intersection of two or more sets
# intersection_update()	            - removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	                    - returns whether two sets have a intersection or not
# issubset()	                    - returns whether another set contains this set or not
# issuperset()	                    - returns whether this set contains another set or not
# pop()	                            - removes an element from the set
# remove()	                        - removes the specified element
# symmetric_difference()	        - returns a set with the symmetric differences of two sets
# symmetric_difference_update()	    - inserts the symmetric differences from this set and another
# union()	                        - return a set containing the union of sets
# update()	                        - update the set with another set, or any other iterable

###########################################################################################################################################
