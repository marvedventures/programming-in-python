###########################################################################################################################################
# PYTHON LIST
###########################################################################################################################################

# LIST
# - sequence of one or more different or similar datatypes
# - essentially a dynamic array that can hold any datatype
# - index based (0 start)

list1 = [1, 2, 3, 4, 5]

list2 = ['A', 'B', 'C', 'D', 'E']

list3 = ['Hello', 1, True, 40.22]

list4 = [1, [2, 3, 4], 5, 6]


print(list1)  # [1, 2, 3, 4, 5]
print(*list1)  # prints the entire elements # 1 2 3 4 5

# Add elements at the end
list1.insert(len(list1), 6)
print(list1)  # [1, 2, 3, 4, 5, 6]
list1.append(7)
print(list1)  # [1, 2, 3, 4, 5, 6, 7]
# argument must be a an iterable(list, tuple, string etc.)
list1.extend([8, 9, 10])
print(list1)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Remove elements
# pop() -  argument is the position of the element you want to remove, default value is -1, which returns the last item
list1.pop()
print(list1)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
list1.pop(4)
print(list1)  # [1, 2, 3, 4, 6, 7, 8, 9]
# del
del list1[3]
print(list1)  # [1, 2, 3, 6, 7, 8, 9]

###########################################################################################################################################

# ITERATING THROUGH A LIST

my_list = ['A', 'B', 'C', 'D', 'E']

# ONLY ELEMENTS/ ITEM
for item in my_list:
    print(item)
    # A
    # B
    # C
    # D
    # E

# WITH INDEX AND ITEM (using enumerate())
for idx, item in enumerate(my_list):
    print(idx, item)
    # 0 A
    # 1 B
    # 2 C
    # 3 D
    # 4 E

###########################################################################################################################################

# LIST BUILT-IN METHODS

# append()	    - adds an element at the end of the list
# clear()	    - removes all the elements from the list
# copy()	    - returns a copy of the list
# count()	    - returns the number of elements with the specified value
# extend()	    - add the elements of a list (or any iterable), to the end of the current list
# index()	    - returns the index of the first element with the specified value
# insert()	    - adds an element at the specified position
# pop()	        - removes the element at the specified position
# remove()	    - removes the first item with the specified value
# reverse()	    - reverses the order of the list
# sort()	    - sorts the list

###########################################################################################################################################
