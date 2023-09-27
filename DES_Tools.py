"""
    This python file contains all the tool functions used in DES algorithm
"""


# This function is used to transform a string into a binary matrix
def ASCII_to_BinaryMatrix(input_str):
    result = ''
    final_result = []
    result_list = []
    for character in input_str:
        # check if the ASCII code of this character is within the range of 0 and 255
        if ord(character) < 0 or ord(character) >= 256:
            return False, None
        else:
            # convert character into a binary string
            char_data = bin(int(str(ord(character)), 10))
            # remove the prefix
            char_data = char_data[2:]
            if len(char_data) < 8:
                char_data = char_data.rjust(8, '0')
            result = result + char_data
    if len(result) % 64 > 0:
        # add 0 before those which do not approach 8 characters
        result = result.rjust(64 * ((len(result) // 64) + 1), '0')
    for point in range(0, len(result)):
        result_list.append(int(result[point]))
        if (point + 1) % 8 == 0:
            final_result.append(result_list)
            result_list = []
    return True, final_result


# This function is used to transform a binary matrix into a string
def Binary_to_Text(binary_matrix):
    final_result = ''
    for data in binary_matrix:
        number = int(data, 2)
        final_result += chr(number)
    return final_result


# This function is used to get the (row, column) positional coordinate from a single number positional coordinate
def get_Location(pos, row):
    pos = pos - 1
    x = int(pos / row)
    y = pos % row
    return [x, y]


# This function is used to convert a matrix with a * b size into a matrix with x * y size
def convert_matrix(source_matrix, a, b, x, y):
    if a * b != x * y:
        # check if the conversion is possible
        return False, None
    list_overall = []
    final_result = []
    result = []
    # extract all the data in source matrix
    for source_list in source_matrix:
        for data in source_list:
            list_overall.append(data)
    # form a matrix with size of x * y
    for point in range(1, x * y + 1):
        result.append(list_overall[point - 1])
        if point % y == 0:
            final_result.append(result)
            result = []
    return final_result


# This function is used to break longer text (larger than 8 chars) into multiple sub lists
def break_text(input_text):
    final_result = []
    result_str = ""
    for pointer in range(len(input_text)):
        result_str += str(input_text[pointer])
        if (pointer + 1) % 8 == 0:
            final_result.append(result_str)
            result_str = ""
    if result_str != "":
        # in case empty string is appended into the list
        final_result.append(result_str)
    return final_result
