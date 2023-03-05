###########################################################################################################################################
# METHOD RESOLUTION ORDER IN ACTION
###########################################################################################################################################

# Example 1
class A:
    def a(self):
        return 'Function inside A'


class B:
    def a(self):
        return 'Function inside B'


class C(B, A):
    pass


# Driver code
c = C()
print(c.a())  # Function inside B

print(C.mro())
# [<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]

###########################################################################################################################################


# Example 2
class A:
    def b(self):
        return 'Function inside A'


class B:
    def b(self):
        return 'Function inside B'


class C(A, B):
    def b(self):
        return 'Function inside C'


class D(C):
    pass


d = D()
print(d.b())  # Function inside C

print(D.mro())
# [<class '__main__.D'>, <class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]

###########################################################################################################################################


# Example 3
class A:
    def b(self):
        return 'Function inside A'


class B:
    def b(self):
        return 'Function inside B'


class C(A, B):
    pass


class D(C):
    pass


d = D()
print(d.b())  # Function inside A

print(D.mro())
# [<class '__main__.D'>, <class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]

###########################################################################################################################################


# Example 4
'''
class A:
    def c(self):
        return 'Function inside A'


class B:
    def c(self):
        return 'Function inside B'


class C(A, B):
    def c(self):
        return 'Function inside C'


class D(A, C):
    pass


d = D()
print(d.a)
'''

'''
TypeError: Cannot create a consistent method resolution order (MRO) for bases A, C

Note that this throws an error. In the code above, class D inherits from both class A and class C.

Class C is its immediate superclass, but since this is multiple inheritance, the rules are more complicated and it also has to check the classes passed to it for precedence.

In this particular case, class D is unable to resolve the order that should be followed, while resolving the value for the variable in cases where the variable is not present in the class of the given object.

It results in a TypeError because it's unable to create method resolution order (MRO). MRO is Python’s way of resolving the order of precedence of classes while dealing with inheritance.
'''

###########################################################################################################################################


# Example 5
class A:
    def d(self):
        return 'Function inside A'


class B:
    def d(self):
        return 'Function inside B'


class C:
    def d(self):
        return 'Function inside C'


class D(A, B):
    def d(self):
        return 'Function inside D'


class E(B, C):
    def d(self):
        return 'Function inside E'


class F(E, D, C):
    pass


f = F()
print(f.d())  # Function inside E

print(F.mro())
# [<class '__main__.F'>, <class '__main__.E'>, <class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>]
