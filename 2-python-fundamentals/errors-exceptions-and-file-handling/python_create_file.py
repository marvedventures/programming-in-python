###########################################################################################################################################
# PYTHON CREATE FILES
###########################################################################################################################################

# write() -> one line
# writelines() -> multiple lines inside a list, to make a new line -> \n

###########################################################################################################################################

# 'w' -> will overwrite existing file

with open('./2-python-fundamentals/errors-exceptions-and-file-handling/create_file.txt', 'w') as file:
    file.writelines(['Hello World\n', 'Hello World 123\n'])


# 'a' -> will create/ append a new line at the end

with open('./2-python-fundamentals/errors-exceptions-and-file-handling/create_file.txt', 'a') as file:
    file.writelines(['Hello World 1234\n', 'Hello World 123456\n'])
    file.write('Hello')

###########################################################################################################################################

# EXCEPTION HANDLING ON FILES

try:
    with open('fake_dir/create_file.txt', 'w') as file1:
        file1.writelines(['Hello World\n', 'Hello World 123\n'])
except FileNotFoundError as e:
    print('ERROR', e)
    # ERROR [Errno 2] No such file or directory: 'fake_dir/create_file.txt'

###########################################################################################################################################
