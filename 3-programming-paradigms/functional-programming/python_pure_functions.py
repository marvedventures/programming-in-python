###########################################################################################################################################
# PURE FUNCTIONS
###########################################################################################################################################

# Pure Functions - no effect beyond its own scope

###########################################################################################################################################

# Traditional Function

my_list = [1, 2, 3, 4]


def add_to_list(list, item):
    return list.append(item)


add_to_list(my_list, 5)

print(my_list)  # [1,2,3,4,5]
# add_to_list function has EFFECT beyond its own scope
# my_list is a global variable
# add_to_list function appends an element to a global variable so it's a traditional function

###########################################################################################################################################

# Pure Function

my_list = [1, 2, 3, 4]


def add_to_list_pure(list, item):
    temp_list = list.copy()
    temp_list.append(item)
    return temp_list


new_list = add_to_list_pure(my_list, 5)

print(my_list)  # [1,2,3,4]
print(new_list)  # [1,2,3,4,5]

# add_to_list_pure function has NO effect beyond its own scope

###########################################################################################################################################
