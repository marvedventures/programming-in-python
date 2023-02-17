
# VARIABLE NAMING CONVENTIONS

# CamelCase

myVariable = 1

# snake_case

my_variable = 1

###########################################################################################################################################

# DECLARING AND RE-ASSIGNING VARIABLE

# Declaring
name = 'Marvin'
print(name)  # 'Marvin'

# Re-assigning
name = 'John'
print(name)  # 'John'

###########################################################################################################################################

# DECLARING MULTIPLE VARIABLE AND ASSIGNING TO ONE VALUE

a = b = c = 10
print(a, b, c)  # 10, 10, 10

###########################################################################################################################################

# MULTIPLE ASSIGNMENTS

a, b, c = 1, 2, 3
print(a)  # 1
print(b)  # 2
print(c)  # 3

###########################################################################################################################################

# DELETING A VARIABLE (del)

last_name = 'Mahomes'

print(last_name)  # 'Mahomes'

del last_name

print(last_name)  # NameError: name 'last_name' is not defined
