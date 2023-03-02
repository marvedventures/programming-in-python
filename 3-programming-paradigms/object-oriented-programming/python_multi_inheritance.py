###########################################################################################################################################
# PYTHON MULTI-LEVEL INHERITANCE
###########################################################################################################################################

# Example 1
class A:
    a = 1


class B:
    b = 2


class C(A, B):
    pass


c = C()
print(c.a, c.b)  # 1 2

###########################################################################################################################################

# Example 2


class A:
    a = 1


class B(A):
    a = 2


class C(B):
    pass


c = C()
print(c.a)  # 2
# The output is 2 because C derives from the immediate super class of C, and that's B.


###########################################################################################################################################

# BUILT-IN FUNCTIONS : issubclass() and isinstance()

# 1. issubclass(A,B)
# -> can be read as 'Is A a subclass of B?'

class A:
    a = 1


class B(A):
    a = 2


class C(B):
    pass


c = C()
print(c.a)

print(issubclass(A, B))
# is A a subclass of B? -> False
print(issubclass(B, A))
# is B a subclass of A? -> True


# 2. isinstance(b, B)
# -> can be read as 'Is b an instance of B?'

class A:
    pass


class B(A):
    pass


b = B()
print(isinstance(b, B))
# is b an istance of B? -> True

###########################################################################################################################################

# super():
# -> gives child an access to parent's/siblings' variables and methods
# -> returns an object that represents the parent class

# USE CASE:
# 1. Allows us to avoid using the base class name explicitly
# 2. Working with Multiple Inheritance


# Example 1: super() with Single Inheritance
# -> In the case of single inheritance, we use super() to refer to the base class.

class Mammal(object):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')


class Dog(Mammal):
    def __init__(self):
        print('Dog has four legs.')
        super().__init__('Dog')


d1 = Dog()

# OUTPUT :
# Dog has four legs.
# Dog is a warm-blooded animal.

'''
Here, we called the __init__() method of the Mammal class (from the Dog class) using code

super().__init__('Dog')
instead of

Mammal.__init__(self, 'Dog')
'''


# Example 2: super() with Multiple Inheritance

class Animal:
    def __init__(self, Animal):
        print(Animal, 'is an animal.')


class Mammal(Animal):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')
        super().__init__(mammalName)


class NonWingedMammal(Mammal):
    def __init__(self, NonWingedMammal):
        print(NonWingedMammal, "can't fly.")
        super().__init__(NonWingedMammal)


class NonMarineMammal(Mammal):
    def __init__(self, NonMarineMammal):
        print(NonMarineMammal, "can't swim.")
        super().__init__(NonMarineMammal)


class Dog(NonMarineMammal, NonWingedMammal):
    def __init__(self):
        print('Dog has 4 legs.')
        super().__init__('Dog')  # 'Dog' called here


d = Dog()  # 'Dog' not called here

# Dog has 4 legs.
# Dog can't swim.
# Dog can't fly.
# Dog is a warm-blooded animal.
# Dog is an animal.

bat = NonMarineMammal('Bat')  # 'Bat' called here
# Bat can't swim.
# Bat is a warm-blooded animal.
# Bat is an animal.

###########################################################################################################################################
