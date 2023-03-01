###########################################################################################################################################
# PYTHON CUSTOM OBJECT
###########################################################################################################################################

# 2 SPECIAL METHODS USED DURING OBJECT CREATION

# 1. __new__ : responsible for creating and returning a new empty object
# 2. __init__: responsible for initializing the object's state (constructor)

class MyClass:
    # cls is not a keyword but only a convention that acts as placeholder
    def __new__(cls, *args, **kwargs):
        print('Creating new instance')
        instance = super().__new__(cls)
        return instance

    # self is 'this' keyword in other programming languages
    def __init__(self, name):
        print('Initializing object')
        self.name = name


my_object = MyClass('Alice')

'''
OUTPUT: 
Creating new instance
Initializing object

When we run the code, we see that the __new__ method is called first to create the instance, followed by the __init__ method to initialize the object.
'''

###########################################################################################################################################

# EXAMPLE 1: CREATING A RECIPE CLASS AND CUSTOM OBJECTS


class Recipe:
    def __init__(self, dish, items, time):
        self.dish = dish
        self.items = items
        self.time = time

    def contents(self):
        print(
            f'The {self.dish} has {self.items} and takes {self.time} to prepare.')
        # print('The ' + self.dish + ' has ' + str(self.items) + ' and takes ' + str(self.time) + ' to prepare. ')


# pizza object
pizza = Recipe('Pizza', ['cheese', 'bread', 'tomato'], 45)
print(pizza.items)
pizza.contents()

# pasta object
pasta = Recipe('Pasta', ['penne', 'sauce'], 55)
print(pasta.items)
pasta.contents()

###########################################################################################################################################

# EXAMPLE 2


class MyFirstClass:
    print('Who wrote this?')
    # note: index is class variable
    index = 'Author Book'

    def hand_list(self, philosopher, book):
        # class variables are accessed directly by calling it over the class name using dot notation.
        print(MyFirstClass.index)
        print(f'{philosopher} wrote the book: {book}')


whodunnit = MyFirstClass()
whodunnit.hand_list('Sun Tzu', 'The Art of War')

###########################################################################################################################################
