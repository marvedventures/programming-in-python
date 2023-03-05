###########################################################################################################################################
# METHOD RESOLUTION ORDER
###########################################################################################################################################

# explain the rules of mro
# explain concept of code linearization
# deploy mro functions

# 5 TYPES OF INHERITANCE
# 1. simple inheritance
# 2. multiple inheritance (inheritance from multiple parents)
# 3. multi-level inheritance (inheritance from several levels)
# 4. hierarchical inheritance (several child class inherit from a common parent)
# 5. hybrid inheritance (mix characteristics)


###########################################################################################################################################

# METHOD RESOLUTION ORDER
# -> determines the order in which a given method or attribute passed is searched

###########################################################################################################################################

# CODE LINEARIZATION
# -> bottom to top, left to right


# ALGORITHMS TO BUILD MRO's
# old -> Depth First Search(DFS)
# new(python 3+) -> C3 Linearization algorithm

# C3 LINEARIZATION ALGORITHM
# -> adheres to monotonicity : an inherited property cannot skip over direct parent classes
# -> follows inheritance graph
# -> visits super class after local classes

###########################################################################################################################################

# MRO FUNCTIONS


# 1. mro()
class A:
    pass


class B(A):
    pass


class C(B):
    pass


print(C.mro())
# OUTPUT:
# [<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]

###########################################################################################################################################

# 2. help() -> more detailed output with MRO info

print(help(C))
# OUTPUT:
# Help on class C in module __main__:

# class C(B)
#  |  Method resolution order:
#  |      C
#  |      B
#  |      A
#  |      builtins.object
#  |
# -- More  --

###########################################################################################################################################
