###########################################################################################################################################
# PYTHON OOP
###########################################################################################################################################

from abc import ABC, abstractmethod

# PYTHON -> primarily OOP, but can be procedural, functional, etc.

# OBJECT-ORIENTED PROGRAMMING
# has high modularity -> easier to understand, reusable, abstraction move between projects

###########################################################################################################################################

# OOP KEY COMPONENTS:

# 1. Classes
# -> blueprint for an object
# class -> defined with 'class' keyword
# attributes -> can be variables
# behavior -> can be functions, methods

# 2. Objects
# -> instance of a class
# instantiation : creating an instance of a class

# 3. Methods
# -> behavior of an object instance

###########################################################################################################################################

# OOP PRINCIPLES

# 1. Inheritance
# -> creating a new class which is derivative of an existing one.
# -> defining a new class that inherits from an existing class
# -> reuse common logic


class Parent:
    pass


class Child(Parent):
    pass


# 2. Polymorphism
# -> ability of a function to change its behavior when called by different objects
# -> child class can overwrite a method inherited from a parent class

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print('Woof!')


class Cat(Animal):
    def make_sound(self):
        print('Meow!')


class Cow(Animal):
    def make_sound(self):
        print('Moo!')


def animal_sounds(animals):
    for animal in animals:
        animal.make_sound()


my_dog = Dog('Fido')
my_cat = Cat('Whiskers')
my_cow = Cow('Betsy')

animal_sounds([my_dog, my_cat, my_cow])


# 3. Encapsulation
# -> limits access to method and variables by encasing them in a single unit of scope (In the case of Python, this unit is called a class)
# -> achieved through the use of access modifiers on attributes and methods of a class.
# The most common access modifiers are public, protected, and private.

# Access Modifiers:

# a. public
# -> can be accessed from anywhere, inside or outside the class.
# -> In Python, all atrributes and methods are public by default (public)


# b. protected
# -> can be accessed only within the class and its subclasses
# -> single underscore at the beginning of the name (_protected)

# c. private
# -> can be accessed only within the class
# -> double underscore at the beginning of the name (__private)

class Alpha:

    def __init__(self):
        self._a = 2.  # Protected member ‘a’
        self.__b = 2.  # Private member ‘b’

# NOTE:
# private and protected members can still be accessed from outside of the class by using public methods to access them or by a practice known as name mangling
# Name Mangling: ->  use of two leading underscores and one trailing underscore, e.g: _class__identifier
# class is the name of the class and identifier is the data member that I want to access.


# 4. Abstraction
# -> hides implementation details for data security
# -> In Python, does not support abstraction directly and uses inheritance to achieve it
# -> In Python, abstraction is typically achieved through the use of abstract classes and abstract methods.
# -> abstract class : can't be instantiated
# -> abstract method : not implemented, but must be implemented by a subclass
# Decorators (@) : add functionality to existing code, without changing the original code.


# the ff imports are already imported above:
# from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print('Woof!')


class Cat(Animal):
    def make_sound(self):
        print('Meow!')


my_dog = Dog('Fido')
my_cat = Cat('Whiskers')

# This would raise an error, as Animal is an abstract class
# my_animal = Animal('Generic Animal')

my_dog.make_sound()
my_cat.make_sound()

###########################################################################################################################################
