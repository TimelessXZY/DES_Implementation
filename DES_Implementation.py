"""
    This python file contains the core encryption & decryption functions and tables used in DES
"""


from DES_Tools import *
# ip table used for initial permutation
IP = [
    [58, 50, 42, 34, 26, 18, 10, 2],
    [60, 52, 44, 36, 28, 20, 12, 4],
    [62, 54, 46, 38, 30, 22, 14, 6],
    [64, 56, 48, 40, 32, 24, 16, 8],
    [57, 49, 41, 33, 25, 17, 9, 1],
    [59, 51, 43, 35, 27, 19, 11, 3],
    [61, 53, 45, 37, 29, 21, 13, 5],
    [63, 55, 47, 39, 31, 23, 15, 7]
]
# E table used in E expansion
E = [
    [32, 1, 2, 3, 4, 5],
    [4, 5, 6, 7, 8, 9],
    [8, 9, 10, 11, 12, 13],
    [12, 13, 14, 15, 16, 17],
    [16, 17, 18, 19, 20, 21],
    [20, 21, 22, 23, 24, 25],
    [24, 25, 26, 27, 28, 29],
    [28, 29, 30, 31, 32, 1]
]
# P table used in P box substitute
P = [
    [16, 7, 20, 21],
    [29, 12, 28, 17],
    [1, 15, 23, 26],
    [5, 18, 31, 10],
    [2, 8, 24, 14],
    [32, 27, 3, 9],
    [19, 13, 30, 6],
    [22, 11, 4, 25]
]
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
# Inverse permutation table
IP_Inverse = [
    [40, 8, 48, 16, 56, 24, 64, 32],
    [39, 7, 47, 15, 55, 23, 63, 31],
    [38, 6, 46, 14, 54, 22, 62, 30],
    [37, 5, 45, 13, 53, 21, 61, 29],
    [36, 4, 44, 12, 52, 20, 60, 28],
    [35, 3, 43, 11, 51, 19, 59, 27],
    [34, 2, 42, 10, 50, 18, 58, 26],
    [33, 1, 41, 9, 49, 17, 57, 25]
]

# ----- plain text processing -----
# This function is used for initial permutation
def initial_permutation(plain_txt):
    final_result = []
    result = []
    for pointer in range(1, 65):
        current_pos = IP[get_Location(pointer, 8)[0]][get_Location(pointer, 8)[1]]
        result.append(plain_txt[get_Location(current_pos, 8)[0]][get_Location(current_pos, 8)[1]])
        if pointer % 8 == 0:
            final_result.append(result)
            result = []
    return final_result


# This function is used to split left and right parts of original text
def left_right_split(input_txt):
    l = []
    r = []
    step = 0
    for pointer in input_txt:
        step = step + 1
        if step <= 4:
            l.append(pointer)
        else:
            r.append(pointer)
    return l, r


# This function is used to expand right source text data from 32 bits to 48 bits
def E_Expansion(right0):
    converted_matrix = convert_matrix(right0, 4, 8, 8, 4)
    final_result = []
    result = []
    for pointer in range(1, 48 + 1):
        current_pos = E[get_Location(pointer, 6)[0]][get_Location(pointer, 6)[1]]
        result.append(converted_matrix[get_Location(current_pos, 4)[0]][get_Location(current_pos, 4)[1]])
        if pointer % 6 == 0:
            final_result.append(result)
            result = []
    return final_result


# This function is used to perform xor operation between 48-bit data and 16 48-bit keys
def xor_right_key(right0_extend, sub_key, times):
    final_result = []
    result_list = []
    result = []
    for pointer in range(1, len(right0_extend) * len(right0_extend[0]) + 1):
        data = sub_key[get_Location(pointer, 6)[0]][get_Location(pointer, 6)[1]] ^ right0_extend[get_Location(pointer, 6)[0][
            get_Location(pointer, 6)[1]
        ]]
        result_list.append(data)
    for pointer in range(1, len(result_list) + 1):
        result.append(result_list[pointer - 1])
        if pointer % 6 == 0:
            final_result.append(result)
            result = []
    return final_result


# This function is used for substitute operation using s boxes
def S_substitute(sub_key):
    final_result = []
    result = []
    for pointer in range(1, len(sub_key) + 1):
        text_line = str(sub_key[pointer - 1][0]) + str(sub_key[pointer - 1][5])
        text_row = str(sub_key[pointer - 1][1]) + str(sub_key[pointer - 1][2]) + \
        str(sub_key[pointer - 1][3]) + str(sub_key[pointer - 1][4])
        line_num = int(text_line, 2)
        row_num = int(text_row, 2)
        source_pos = S[pointer - 1][line_num][row_num]
        cur_data = bin(source_pos)
        cur_data = cur_data[2:]
        real_data = cur_data.rjust(4, '0')
        for chars in real_data:
            result.append(int(chars))
        final_result.append(result)
        result = []
    return final_result


# This function is used for substitute operation using p table
def P_substitute(S_result, left0, times):
    final_result = []
    result_list = []
    result = []
    for pointer in range(1, len(S_result) * len(S_result[0]) + 1):
        cur_pos = P[get_Location(pointer, 4)[0]][get_Location(pointer, 4)[1]]
        result_list.append(S_result[get_Location(cur_pos, 4)[0]][get_Location(cur_pos, 4)[1]])
    converted_matrix = convert_matrix(left0, 4, 8, 8, 4)
    for pointer in range(1, len(S_result) * len(S_result[0]) + 1):
        cur_data = result_list[pointer - 1] ^ converted_matrix[get_Location(pointer, 4)[0]][get_Location(pointer, 4)[1]]
        result.append(cur_data)
        if pointer % 4 == 0:
            final_result.append(result)
            result = []
    return final_result


# This function is used for iterations (plain text decryption repeated 16 times)
def iterations_16(left_part, right_part, sub_keys):
    # initialize
    l_data, r_data = left_part, right_part
    final_result, temp_data = [], []
    for pointer in range(1, 17):
        l_temp, r_temp = l_data, r_data
        l_data = r_temp
        # E expansion
        extended_right = E_Expansion(r_temp)
        # xor operation
        XORed_right = xor_right_key(extended_right, sub_keys[pointer - 1], pointer)
        # S substitution
        S_substituted = S_substitute(XORed_right)
        # P substitution
        r_data = P_substitute(S_substituted, l_temp, pointer)
    for data_list in r_data:
        temp_data.append(data_list)
    for data_list in l_data:
        temp_data.append(data_list)

    temp = []
    for pointer in range(1, len(temp_data) * len(temp_data[0]) + 1):
        temp.append(temp_data[get_Location(pointer, 4)[0]][get_Location(pointer, 4)[1]])
        if pointer % 8 == 0:
            final_result.append(temp)
            temp = []
    return final_result


# This function is used for inverse permutation
def IP_1_substitute(iterated_result):
    final_result, temp_str, resultList, tempList = [], "", [], []
    for pointer in range(1, len(iterated_result) * len(iterated_result[0]) + 1):
        cur_pos = IP_Inverse[get_Location(pointer, 8)[0]][get_Location(pointer, 8)[1]]
        temp_str += str(iterated_result[get_Location(cur_pos, 8)[0]][get_Location(cur_pos, 8)[1]])
        tempList.append(iterated_result[get_Location(cur_pos, 8)[0]][get_Location(cur_pos, 8)[1]])
        if pointer % 8 == 0:
            final_result.append(temp_str)
            resultList.append(tempList)
            temp_str = ""
            tempList = []
    return  final_result, resultList


# ----- keys and sub-keys generation process -----
# This function is used to remove the last column of secret key binary matrix
def remove_lastColumn(input_secretKey):
    final_result = []
    for data_list in input_secretKey:
        data_list.pop()
        final_result.append(data_list)
    return final_result


# This function is used in secret key PC 1 substitution
def PC1_substitute(removed_secretKey):
    final_result, temp = [], []
    for pointer in range(1, 57):
        cur_pos = PC_1[get_Location(pointer, 7)[0]][get_Location(pointer, 7)[1]]
        temp.append(removed_secretKey[get_Location(cur_pos, 8)[0]][get_Location(cur_pos, 8)[1]])
        if pointer % 7 == 0:
            final_result.append(temp)
            temp = []
    return final_result


# This function is used in secret key PC 2 substitution
def PC2_substitute(substituted_secretKey):
    final_result, temp = [], []
    for pointer in range(1, 49):
        cur_pos = PC_2[get_Location(pointer, 6)[0]][get_Location(pointer, 6)[1]]
        temp.append(substituted_secretKey[get_Location(cur_pos, 7)[0]][get_Location(cur_pos, 7)[1]])
        if pointer % 6 == 0:
            final_result.append(temp)
            temp = []
    return final_result


# This function is used to left-move operation in generating secret keys (a single round)
def move_left(key_left, key_right, round):
    steps, left_part, right_part, sum_all, result = 2, [], [], [], []
    temp_list, resultLeft, resultRight = [], [], []
    # check if the round num is correct
    if round not in range(1, 17):
        return False, None, None
    else:
        if round in [1, 2, 9, 16]:
            steps = 1
        else:
            steps = 2
    # turn C part of secret key into list
    for pointer in range(1, len(key_left) * len(key_left[0]) + 1):
        left_part.append(key_left[get_Location(pointer, 7)[0]][get_Location(pointer, 7)[1]])
    # turn D part of secret key into list
    for pointer in range(1, len(key_right) * len(key_right[0]) + 1):
        right_part.append(key_right[get_Location(pointer, 7)[0]][get_Location(pointer, 7)[1]])
    # left-move operation for C part
    for i in range(steps):
        left_part.insert(len(left_part), left_part[0])
        left_part.remove(left_part[0])
    # left-move operation for D part
    for i in range(steps):
        right_part.insert(len(right_part), right_part[0])
        right_part.remove(right_part[0])

    sum_all.extend(left_part)
    sum_all.extend(right_part)

    # generate new sub keys
    for pointer in range(1, len(sum_all) + 1):
        temp_list.append(sum_all[pointer - 1])
        if pointer % 7 == 0:
            result.append(temp_list)
            temp_list = []
    # new C part
    for pointer in range(1, len(left_part) + 1):
        temp_list.append(left_part[pointer - 1])
        if pointer % 7 == 0:
            resultLeft.append(temp_list)
            temp_list = []
    # new D part
    for pointer in range(1, len(right_part) + 1):
        temp_list.append(right_part[pointer - 1])
        if pointer % 7 == 0:
            resultRight.append(temp_list)
            temp_list = []
    return result, resultLeft, resultRight


# This function is used to generate 16 sub keys after left-move operation
def generate_subKeys(C_part, D_part):
    left, rigjt = C_part, D_part
    final_result = []
    for round in range(1, 17):
        # firstly, left-move operation
        left_secretKey, l, r = move_left(left, rigjt, round)
        # secondly, PC-2 substitution
        pc2_secretKey = PC2_substitute(left_secretKey)
        final_result.append(pc2_secretKey)
    return final_result


# This function is the entire pipeline of generating keys
def keys_generation_pipeline(key):
    if len(key) > 8:
        key = key[0:8]
    # get key from users
    secret_state, secret_key_binary = ASCII_to_BinaryMatrix(key)
    # compress key
    secret_key_binary = remove_lastColumn(secret_key_binary)
    # PC1 substitution
    secret_key_binary = PC1_substitute(secret_key_binary)
    # split secret key into left and right parts
    left_secretKey, right_secretKey = left_right_split(secret_key_binary)
    # generate all the sub keys
    subkey_collection = generate_subKeys(left_secretKey, right_secretKey)
    return subkey_collection
