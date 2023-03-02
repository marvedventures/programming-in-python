###########################################################################################################################################
# PARENT CLASSES VS. CHILD CLASSES
###########################################################################################################################################

# Parent : Parent/Super/Base Class
# Child : Child/Sub/Derived Class

# -> child class being derived from a parent class (inheritance)
# -> child class extends attributes(variables) and behaviors(methods) of parent
# -> child class alows: add more props to child class and modify inherited properties in child class w/o affecting the parent


###########################################################################################################################################

# INHERITANCE IN ACTION: EMPLOYEE MANAGEMENT

class Employee:
    def __init__(self, first, last) -> None:
        self.first = first
        self.last = last


# if child will add a new attribute(variable), call init then inside it call super() first (to access first, and last variable in parent)
class Supervisors(Employee):
    def __init__(self, first, last, password) -> None:
        super().__init__(first, last)
        self.password = password


#  if child won't add new attributes(variable), no need for init()
class Chefs(Employee):
    def leave_request(self, days):
        return f'May I take the leave for {days} days'


adrian = Supervisors('Adrian', 'J', 'apple')
emily = Chefs('Emily', 'E')
joanna = Chefs('Joanna', 'J')

print(adrian.password)  # apple
print(adrian.first)  # Adrian
print(emily.leave_request(3))  # May I take the leave for 3 days
print(joanna.first)  # Joanna

###########################################################################################################################################
