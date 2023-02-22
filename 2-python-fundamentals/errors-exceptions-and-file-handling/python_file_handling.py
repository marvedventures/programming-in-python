###########################################################################################################################################
# PYTHON FILE HANDLING
###########################################################################################################################################

# OPEN()

# open(<file name> <file location>, <mode>)
# mode - action: reading/writing/creating ; output format: text/binary

# Mode sets -> reading is the default action and text is the default output format

# 'r' -> open for reading (text)
# 'rb' ->  open for reading (binary)

# 'r+' -> open for reading and writing (text)
# 'rb+' -> open for reading and writing (binary)

# 'w' -> open for writing (text), will overwrite the existing file
# 'wb' -> open for writing (binary), will overwrite the existing file

# 'a' -> open for editing, appending data

###########################################################################################################################################

# CLOSE

# close() -> no arguments

###########################################################################################################################################

# WITH OPEN

# with open ('testing.txt', 'r') as file:
# no close functions needed ; automatically closed
# better for exception handling
# can also loop through the file and print the text line by line:

###########################################################################################################################################

# OPEN AND CLOSE IN PRACTICE

file = open(
    './2-python-fundamentals/errors-exceptions-and-file-handling/test.txt', 'r')

# readline only read one first line
data = file.readline()
# H

# readlines read the lines and outputs an array
data1 = file.readlines()
# ['He\n', 'Hell\n', 'Hello\n', 'Hello W\n', 'Hello Wo\n', 'Hello Wor\n', 'Hello Worl\n', 'Hello World']

print(data)
print(data1)

file.close()

# if a method is called after a closefile
# data1 = file.readlines() # ValueError: I/O operation on closed file.

###########################################################################################################################################

# WITH OPEN IN PRACTICE

with open('./2-python-fundamentals/errors-exceptions-and-file-handling/test.txt', 'r') as file1:
    data2 = file1.readlines()

    print(data2)
    # ['H\n', 'He\n', 'Hell\n', 'Hello\n', 'Hello W\n', 'Hello Wo\n', 'Hello Wor\n', 'Hello Worl\n', 'Hello World']

###########################################################################################################################################
