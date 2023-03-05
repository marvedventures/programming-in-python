###########################################################################################################################################
# PYTHON NAMESPACING AND SCOPING
###########################################################################################################################################

# NAMESPACING -> Name (which means name, a unique identifier) + Space(which talks something related to scope)
# 1. LOCAL -> creation of local functions
# 2. GLOBAL -> user creates a module
# 3. BUILT-IN -> print(), id()

# SCOPING -> LEGB
# 1. LOCAL -> inside a function
# 2. ENCLOSED -> inside a nested function
# 3. GLOBAL -> upper level (outside of function)
# 4. BUILT-IN -> keywords present in a built in module

###########################################################################################################################################

def d():
    animal = 'elephant'

    def e():
        nonlocal animal
        animal = 'giraffe'
        print('Inside a nested function: ' + animal)

    print('Before calling the function: ' + animal)
    e()
    print('After calling the function: ' + animal)


animal = 'camel'
d()
print('Global animal: ' + animal)

# Before calling the function: elephant
# Inside a nested function: giraffe
# After calling the function: giraffe
# Global animal: camel

###########################################################################################################################################
