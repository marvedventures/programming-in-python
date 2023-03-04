###########################################################################################################################################
# ABSTRACT CLASSES AND METHODS
###########################################################################################################################################

# ABSTRACT CLASSES:
# hide implementation details w/o sacrificing functionality -> a) methods must be implemented in child class/ b) super function()
# abstract classes act only as a base class for other classes to derive from.
# abstract classes can exist with / without abstract methods present inside them

# limitations:
# can't create instance
# no direct implementation of abstraction in Python (must import abc module and use inheritance)
# methods must be defined before it can be implemented
# abstract class can't be instantiated

###########################################################################################################################################

# steps:
# 1. import Abstract Base Class (ABC), and abstract method decorator from abc module
# 2. create inheriting class (this will be the abstract class)
# 3. define abstract method (no implementation)
# 4. abstract method must be implemented in child class
# 5. child of abstract class can be instantiated if all abstract methods are implemented


# 1
from abc import ABC, abstractmethod


# 2
class Vehicle(ABC):
    # 3
    @abstractmethod
    def start_engine(self):
        pass

    # 3
    @abstractmethod
    def stop_engine(self):
        pass

# TypeError: Can't instantiate abstract class Vehicle with abstract methods start_engine, stop_engine
# Truck = Vehicle()


class Car(Vehicle):
    # 4
    def start_engine(self):
        print('Starting car engine...')

    # 4
    def stop_engine(self):
        print('Stopping car engine...')


# 5
Lambo = Car()
print(Lambo)


class Motorcycle(Vehicle):
    # 4
    def start_engine(self):
        print('Starting motorcycle engine...')

    # 4
    def stop_engine(self):
        print('Stopping motorcycle engine...')


# 5
Ducati = Motorcycle()
print(Ducati)

# NOTE:
# 1. abstract class -> can have one or more abstract methods, can't be instantiated
# 2. child of abstract class -> can only be instantiated if abstract methods are overriden

###########################################################################################################################################
