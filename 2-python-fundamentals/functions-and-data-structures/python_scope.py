###########################################################################################################################################
# PYTHON SCOPES
###########################################################################################################################################

# 1. LOCAL - variable declared inside a function.
# 2. ENLOSED - variable in a nested function
# 3. GLOBAL - variable is declared outside of a function

# 4. BUILT-IN SCOPE
# - refers to the reserved keywords that Python uses for its built-in functions, such as print, def, for, in, and so forth.
# - functions with built-in scope can be accessed at any level.

# NOTE: ANYTHING on the outside can be accessed inside, NOT the other way around

###########################################################################################################################################

# EXAMPLE

# 1. global scope
global_v = 1


def fn1():
    # 2. enclosed scope
    enlosed_v = 8

    def fn2():
        # 3. local scope
        local_v = 5
        print(local_v)

        print(enlosed_v)
        print(global_v)

    fn2()

    print(enlosed_v)
    print(global_v)


fn1()

print(global_v)
