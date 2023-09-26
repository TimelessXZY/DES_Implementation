"""
    This python file specifies all the tool functions and tables used in DES algorithm
"""
# pc 1 table used in secret key generation
PC_1 = [
    [57, 49, 41, 33, 25, 17, 9],
    [1, 58, 50, 42, 34, 26, 18],
    [10, 2, 59, 51, 43, 35, 27],
    [19, 11, 3, 60, 52, 44, 36],
    [63, 55, 47, 39, 31, 23, 15],
    [7, 62, 54, 46, 38, 30, 22],
    [14, 6, 61, 53, 45, 37, 29],
    [21, 13, 5, 28, 20, 12, 4]
]
# pc 2 table used in secret key generation
PC_2 = [
    [14, 17, 11, 24, 1, 5],
    [3, 28, 15, 6, 21, 10],
    [23, 19, 12, 4, 26, 8],
    [16, 7, 27, 20, 13, 2],
    [41, 52, 31, 37, 47, 55],
    [30, 40, 51, 45, 33, 48],
    [44, 49, 39, 56, 34, 53],
    [46, 42, 50, 36, 29, 32]
]
# 8 S boxes
S_1 = [
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
]
S_2 = [
    [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
    [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
    [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
    [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
]
S_3 = [
    [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
    [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
    [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
    [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
]
S_4 = [
    [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
    [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
    [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
    [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
]
S_5 = [
    [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
    [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
    [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
    [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
]
S_6 = [
    [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
    [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
    [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
    [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
]
S_7 = [
    [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
    [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
    [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
    [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
]
S_8 = [
    [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
    [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
    [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
    [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
]
S = [S_1, S_2, S_3, S_4, S_5, S_6, S_7, S_8]


# This function is used transform a string into a binary matrix
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
