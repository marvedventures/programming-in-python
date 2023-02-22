###########################################################################################################################################
# Read in data, store, manipulate and output new data to a file
###########################################################################################################################################

def read_file(file_name):
    # Reads in a file.
    f = open(file_name)
    f_contents = f.read()
    print(f_contents)
    return f_contents


def read_file_into_list(file_name):
    # Reads in a file and stores each line as an element in a list
    f = open(file_name)
    f_list = f.readlines()
    return f_list


def write_first_line_to_file(file_contents, output_filename):
    # Writes the first line of a string to a file.
    f_line = file_contents.split('\n')[0]
    f = open(output_filename, 'w')
    return f.write(f_line)


def read_even_numbered_lines(file_name):
    # Reads in the even numbered lines of a file
    f = open(file_name)
    f_list = f.readlines()
    even_list = [item for idx, item in enumerate(f_list) if idx % 2 == 1]
    return even_list


def read_file_in_reverse(file_name):
    # Reads a file and returns a list of the lines in reverse order
    f = open(file_name)
    f_list = f.readlines()
    reverse_list = f_list[::-1]
    return reverse_list


# Initialize functions
def main():
    file_contents = read_file(
        './2-python-fundamentals/errors-exceptions-and-file-handling/sampletext.txt')
    print(read_file_into_list(
        './2-python-fundamentals/errors-exceptions-and-file-handling/sampletext.txt'))
    write_first_line_to_file(
        file_contents, './2-python-fundamentals/errors-exceptions-and-file-handling/online.txt')
    print(read_even_numbered_lines(
        './2-python-fundamentals/errors-exceptions-and-file-handling/sampletext.txt'))
    print(read_file_in_reverse(
        './2-python-fundamentals/errors-exceptions-and-file-handling/sampletext.txt'))


if __name__ == '__main__':
    main()
