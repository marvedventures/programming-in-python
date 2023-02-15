# SPACING

# Correct
# any amount of whitespace in a single line is okay
x = 1 + 2
print(x)  # 3

# Incorrect
x = 1
+ 2
print(x)  # 1

###########################################################################################################################################

# INDENTATION

# Correct


def say_hello():
    print("Hello there!")


print(say_hello())


def say_hello(): print("Hello there!")


print(say_hello())

# Incorrect

# def say_hello():
# print("Hello there!")

#     def say_hello():
# print("Hello there")
