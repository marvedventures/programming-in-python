###########################################################################################################################################
# PYTHON PRINT() FUNCTION
###########################################################################################################################################

# PRINT ARGUMENTS

# Comma separated
print(1, 2, 3)  # 1 2 3

# Arithmetic
print(1 + 2)  # 3

# String Concatenation
name = 'John'
print('Hello ' + name)  # Hello John

###########################################################################################################################################

# PYTHON PRINT() FUNCTION's ARGUMENTS

# 1. object(s)
# - that are values printed on screen
# Python support printing of objects and not limited to strings.
# We can easily print list, dictionary, set, tuple and all other objects.

print('1')
print(1)
odd_list = [1, 3, 5, 7]
even_tuple = (2, 4, 6, 8, 10)
print(odd_list, even_tuple)


# 2. sep
# - specifies the separator character between the values to be printed. The default value is a space character.

print('Hello', 'You!', sep=', ')  # Hello, You!
print('Good Morning!', 'Jane', sep=' <3 ')  # Good Morning! <3 Jane


# 3. end
# - specifies the string that should be printed at the end of the output. The default value is a newline character (\n).
# - The general use of end parameter is to combine the output of multiple print function into a single line. Here is the example that demonstrates the same.

# odd_list = [3, 5, 7, 9]
# for el in odd_list:
#     print(el**2, end=' ')
# OUTPUT: 9 25 49 81

# WITHOUT END ARGUMENT,IT WILL BE:
# 9
# 25
# 49
# 81


# 4. file - specifies the file object where the output should be written. The default value is the sys.stdout.

# sample_file = open('hello_world.txt', 'w')
# print("Hello World!", file=sample_file)
# sample_file.close()


# 5. flush: a boolean value that determines whether the output should be flushed immediately or buffered.The default value of the flush parameter is False, which means the buffer will store data until it finds new line character (\n).

# sample_file = open('hello_world.txt', 'w')
# print("Hello World!", file=sample_file, flush=True)

###########################################################################################################################################

# DIRECT FORMATTING

a = 10
b = 5
ans = a + b

print('Adding the value of {} and {} = {}'.format(a, b, ans))
# OUTPUT : Adding the value of 10 and 5 = 15

# can also control the order by specifying the numbers inside the curly brackets

print('I like {} more than {}'.format('oranges', 'apples'))
# OUTPUT: I like oranges more than apples

print('I like {1} more than {0}'.format('oranges', 'apples'))
# OUTPUT: I like apples more than oranges

###########################################################################################################################################
