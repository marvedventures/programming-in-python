###########################################################################################################################################
# WHAT IS FUNCTIONAL PROGRAMMING?
###########################################################################################################################################

# Functional Programming
# - clean
# - consistent
# - maintainable
# - shouldn't change data outside of the function

# Functions
# - take some input, process it and then produce some outputs
# - standalone/ independent
# - first-class citizens (can be assigned to a variable, passed as an arg, returned to its caller)


# Types of Function

# 1. Traditional
# - can access global state
# - can modify global variable
# - can access local state
# - can change args
# - output doesn't depend on input


# 2. Pure
# - can't access global state
# - can't modify global variable
# - can acess local state
# - can't change args
# - output depend on input

###########################################################################################################################################

# FUNCTIONAL PROGRAMMING EXAMPLE

coffees = ['Espresso', 'Latte', 'Cappuccino',
           'Macchiato', 'Americano', 'Decaf']


def reverse(str):
    return str[::-1]


reversed_coffees = map(reverse, coffees)

for item in reversed_coffees:
    print(item)
    # osserpsE
    # ettaL
    # oniccuppaC
    # otaihccaM
    # onaciremA
    # faceD

###########################################################################################################################################
