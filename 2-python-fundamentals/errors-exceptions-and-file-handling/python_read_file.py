###########################################################################################################################################
# PYTHON READ FILES
###########################################################################################################################################

# read()
# -> return a string that contains all the chars
# -> argument: int -> number of chars in a file ; ex. read(40) -> 40 chars, including spaces


# readline()
# return a single line/ first line as a string
# -> argument: int -> number of chars in a file ; ex. readline(40) -> 40 chars, including spaces


# readlines()
# reads the entire content of the file and returns it in an ordered list

###########################################################################################################################################

with open('./2-python-fundamentals/errors-exceptions-and-file-handling/read_file.txt', 'r') as file:

    # data1 = file.read()
    # print(data1)

    # data2 = file.readline()
    # print(data2)

    # can loop over the ouput of readlines() -> list
    # data3 = file.readlines()
    # for item in data3:
    #     print(item)

    # NOTE: using 'with open' and get 'as' file -> it returns a list by default
    for item in file:
        print(item)
