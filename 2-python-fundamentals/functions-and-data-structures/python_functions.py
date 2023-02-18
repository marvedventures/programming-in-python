###########################################################################################################################################
# PYTHON FUNCTIONS
###########################################################################################################################################

# FUNCTIONS -  modular piece of code that can be re-used repeatedly

# Python Function Syntax

def function_name(parameters):
    # function body
    return

# def - keyword used to declare a function
# function_name - any name given to the function
# parameters - any value passed to function
# return (optional) - returns value from a function

###########################################################################################################################################

# PYTHON FUNCTION's PRACTICAL EXAMPLE


def add_tax(bill, tax_rate):
    return bill * tax_rate / 100.00


print(add_tax(175.00, 15))  # 26.25
print(add_tax(135, 10))  # 13.5

###########################################################################################################################################
