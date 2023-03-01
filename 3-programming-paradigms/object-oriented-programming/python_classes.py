###########################################################################################################################################
# PYTHON CLASSES AND INSTANCES
###########################################################################################################################################

# CREATE A CLASS, INSTANTIATE IT AND ACCESS ITS VARIABLES AND METHODS

# creating a class
class MyClass:
    a = 10

    def hello(self):
        print('Hello World!')


# creating an object/ instance of a class
myc = MyClass()

# accessing variables (dot notation)
print(myc.a)

# accessing methods (dot notation)
myc.hello()

###########################################################################################################################################

# EXERCISE: DEFINE A CLASS


class House:
    '''
    This is a stub for a class representing a house that can be used to create objects and evaluate different metrics that we may require in constructing it.
    '''
    num_rooms = 5
    bathrooms = 2

    # Functionality to calculate the costs from the area of the house
    def cost_evaluation(self):
        print(self.num_rooms)
        pass


'''
The code above completely defines the class and functions present inside it, but it is effectively not useful unless you call or instantiate it. You can do this by one of the two ways: a. Calling the class directly, b. Instantiating an object of that class
'''


# a. Calling the class directly
print(House.num_rooms)  # 5
# b. instantiating an object of a House class
house = House()
print(house.num_rooms)  # 5


house.num_rooms = 7
print(house.num_rooms)  # 7
print(House.num_rooms)  # 5
'''
What has happened in the code above is, you have created an instance of a class called house and then modified the attribute for that instance with a value of 7. It updates the value of the instance attribute, but not the class attribute. So the num_rooms attribute of the class remains unchanged as 5, but the instance attribute associated with house object changes to 7
'''

###########################################################################################################################################

# classes are not hoisted, can't call before  its defined

# this would return an error: NameError: name 'B' is not defined.
# bravo = 3
# b = B()
# class B:
#     bravo = 5
#     print("Inside class B")
# c = B()
# print(b.bravo)
