import tkinter as tk

# ip table used for initial permutation
IP = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]
# E table used in E expansion
E = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]
# P table used in P box substitute
P = [
    16, 7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2, 8, 24, 14,
    32, 27, 3, 9,
    19, 13, 30, 6,
    22, 11, 4, 25
]
# pc 1 table used in secret key generation
PC_1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]
# pc 2 table used in secret key generation
PC_2 = [
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]
# 8 S boxes
S_1 = [
    14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
    0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
    4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
    15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13
]
S_2 = [
    15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
    3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
    0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
    13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9
]
S_3 = [
    10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
    13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
    13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
    1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12
]
S_4 = [
    7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
    13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
    10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
    3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14
]
S_5 = [
    2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
    14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
    4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
    11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3
]
S_6 = [
    12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
    10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
    9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
    4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13
]
S_7 = [
    4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
    13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
    1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
    6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12
]
S_8 = [
    13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
    1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
    7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
    2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11
]
S = [S_1, S_2, S_3, S_4, S_5, S_6, S_7, S_8]
# Inverse permutation table
IP_Inverse = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]


# This function is used to convert char to unicode
def char_to_unicode(input_text, length):
    output_text = []
    for i in range(length):
        output_text.append(ord(input_text[i]))
    return output_text


# This function is used to convert unicode to bit
def unicode_to_bit(input_text, length):
    output_bit = []
    for i in range(length * 16):
        output_bit.append(input_text[int(i / 16)] >> (i % 16) & 1)
    return output_bit


# This function is used to convert byte to bit
def byte_to_bit(input_text, length):
    output_bit = []
    for i in range(length * 8):
        output_bit.append(input_text[int(i / 8)] >> (i % 8) & 1)
    return output_bit


# This function is used to convert bit to unicode
def bit_to_unicode(input_bit, length):
    output_bit = []
    recorder = 0
    for i in range(length):
        recorder = recorder | (input_bit[i] << (i % 16))
        if i % 16 == 15:
            output_bit.append(recorder)
            recorder = 0
    return output_bit


# This function is used to convert bit to byte
def bit_to_byte(input_bit, length):
    output_bit = []
    recorder = 0
    for i in range(length):
        recorder = recorder | (input_bit[i] << (i % 8))
        if i % 8 == 7:
            output_bit.append(recorder)
            recorder = 0
    return output_bit


# This function is used to convert unicode to char
def unicode_to_char(source, length):
    output_text = ""
    for i in range(length):
        output_text += chr(source[i])
    return output_text


# This function is used for generating sub keys in iterations
def generate_keys(input_keys):
    sub_keys = []

    # not sure, if the length of key is bigger than 8, then split
    if len(input_keys) > 8:
        input_keys = input_keys[0:8]

    # input keys conversion
    # text keys -> unicode
    ascii_key = char_to_unicode(input_keys, len(input_keys))
    bit_key = byte_to_bit(ascii_key, len(ascii_key))

    # keys initial
    extended_key = [0 for i in range(56)]
    shortened_key = [0 for i in range(48)]

    # PC1 substitute
    for i in range(56):
        extended_key[i] = bit_key[PC_1[i] - 1]

    # 16 iterations of generating sub keys
    for round in range(16):
        # round number determines the moving steps
        if round == 0 or round == 1 or round == 8 or round == 15:
            step = 1
        else:
            step = 2
        # move left operation
        for j in range(step):
            temp = extended_key[0]
            for k in range(27):
                extended_key[k] = extended_key[k + 1]
            extended_key[27] = temp
            temp = extended_key[28]
            for k in range(28, 55):
                extended_key[k] = extended_key[k + 1]
            extended_key[55] = temp

        # PC2 substitute
        for k in range(48):
            shortened_key[k] = extended_key[PC_2[k] - 1]
        sub_keys.extend(shortened_key)
    return sub_keys


# This function organizes all the processes in encryption & decryption pipeline
def DES_pipeline(input_text, input_key, optionType):
    keyResult = generate_keys(input_key)
    # store final text
    finalTextOfBit = [0 for i in range(64)]
    finalTextOfUnicode = [0 for i in range(4)]

    # option type is 0, implements encryption
    if optionType == 0:
        # initial
        tempText = [0 for i in range(64)]

        # enxtend right
        extendR = [0 for i in range(48)]

        # char convert to bit
        unicodeText = char_to_unicode(input_text, len(input_text))
        bitText = unicode_to_bit(unicodeText, len(unicodeText))

        # initialize
        initTrans = [0 for i in range(64)]

        # --------------- IP ---------------
        for i in range(64):
            initTrans[i] = bitText[IP[i] - 1]

        # split as left and right
        L = initTrans[:32]
        R = initTrans[32:]

        # 16 iterations
        for i in range(16):
            tempR = R

            # ------- extend right -------
            for j in range(48):
                extendR[j] = R[E[j] - 1]

            # get sub keys
            keyi = [keyResult[j] for j in range(i * 48, i * 48 + 48)]

            # --------- xor operation --------
            XORResult = [0 for j in range(48)]
            for j in range(48):
                if keyi[j] != extendR[j]:
                    XORResult[j] = 1
            # ----------------------------------

            # --------- s box operations ----------
            SResult = [0 for k in range(32)]
            for k in range(8):
                row = ((XORResult[k * 6]) << 1) | (XORResult[k * 6 + 5])
                column = 0
                for j in range(1, 5):
                    column = column | (XORResult[k * 6 + j] << (4 - j))
                temp = S[k][row * 16 + column]
                for m in range(4):
                    SResult[k * 4 + m] = (temp >> m) & 1
            # ---------------------------------

            # ------------- p box operation -------------
            PResult = [0 for k in range(32)]
            for k in range(32):
                PResult[k] = SResult[P[k] - 1]
            # -----------------------------------------

            # -------------- xor operation ------------
            XORWithL = [0 for k in range(32)]
            for k in range(32):
                if L[k] != PResult[k]:
                    XORWithL[k] = 1
            # ----------------------------------------------

            L = tempR
            R = XORWithL

            # ----------------- end iterations -----------------

        # switch left and right
        L, R = R, L
        tempText = L
        tempText.extend(R)

        # IP inverse
        for k in range(64):
            finalTextOfBit[k] = tempText[IP_Inverse[k] - 1]

        # bit to unicode
        finalTextOfUnicode = bit_to_byte(finalTextOfBit, len(finalTextOfBit))
        finalTextOfChar = unicode_to_char(finalTextOfUnicode, len(finalTextOfUnicode))

        return finalTextOfChar

    # option type is 1, implements decryption
    else:
        # initial
        tempText = [0 for i in range(64)]

        # extend right
        extendR = [0 for i in range(48)]

        # char convert to bit
        unicodeText = char_to_unicode(input_text, len(input_text))
        bitText = byte_to_bit(unicodeText, len(unicodeText))

        # initialize
        initTrans = [0 for i in range(64)]

        # --------------- IP ---------------
        for i in range(64):
            initTrans[i] = bitText[IP[i] - 1]

        # split left and right
        L = [initTrans[i] for i in range(32)]
        R = [initTrans[i] for i in range(32, 64)]

        # 16 iterations
        for i in range(15, -1, -1):
            tempR = R

            # ------- extend right -------
            for j in range(48):
                extendR[j] = R[E[j] - 1]

            # get sub keys
            keyi = [keyResult[j] for j in range(i * 48, i * 48 + 48)]

            # --------- xor operation --------
            XORResult = [0 for j in range(48)]
            for j in range(48):
                if keyi[j] != extendR[j]:
                    XORResult[j] = 1
            # ----------------------------------

            # --------- s boxes operations ----------
            SResult = [0 for k in range(32)]

            for k in range(8):
                row = (XORResult[k * 6] << 1) | (XORResult[k * 6 + 5])
                column = 0
                for j in range(1, 5):
                    column = column | (XORResult[k * 6 + j] << (4 - j))
                temp = S[k][row * 16 + column]
                for m in range(4):
                    SResult[k * 4 + m] = (temp >> m) & 1
            # ---------------------------------

            # ------------- p box operation -------------
            PResult = [0 for k in range(32)]
            for k in range(32):
                PResult[k] = SResult[P[k] - 1]
            # -----------------------------------------

            # -------------- xor operation ------------
            XORWithL = [0 for k in range(32)]
            for k in range(32):
                if L[k] != PResult[k]:
                    XORWithL[k] = 1
            # ----------------------------------------------

            L = tempR
            R = XORWithL

        # switch left and right
        L, R = R, L
        tempText = L
        tempText.extend(R)
        # ---------------------- IP inverse ----------------------
        for k in range(64):
            finalTextOfBit[k] = tempText[IP_Inverse[k] - 1]

        # bit convert to char
        finalTextOfUnicode = bit_to_unicode(finalTextOfBit, len(finalTextOfBit))
        finalTextOfChar = unicode_to_char(finalTextOfUnicode, len(finalTextOfUnicode))

        return finalTextOfChar


# higher-level interface of encryption
def encryption(input_text, input_key, optionType):
    key_length = len(input_key)
    length = len(input_text)
    Result = ""
    input_text = input_text + int(length % 4) * " "
    length = len(input_text)
    if key_length < 8:
        input_key = input_key + int(8 - key_length) * " "
    for i in range(int(length / 4)):
        tempText = [input_text[j] for j in range(i * 4, i * 4 + 4)]
        Result = "".join([Result, DES_pipeline(tempText, input_key, int(optionType))])
    return Result


# higher-level interface of decryption
def decryption(input_text, input_key, optionType):
    key_length = len(input_key)
    length = len(input_text)
    Result = ""
    if key_length < 8:
        input_key = input_key + int(8 - key_length) * " "
    for i in range(int(length / 8)):
        tempText = [input_text[j] for j in range(i * 8, i * 8 + 8)]
        Result = "".join([Result, DES_pipeline(tempText, input_key, int(optionType))])
    return Result


# --------------- user interfaces -----------------
class base():
    def __init__(self, master):
        # basic window setting
        self.root = master
        self.root.config()
        self.root.title('DES Encryption & Decryption')
        self.root.geometry('600x600')
        DES_encryption(self.root)


class DES_encryption():
    def __init__(self, master):
        self.master = master
        self.master.config()
        self.des = tk.Frame(self.master, bg="#e8ded2")
        self.des.pack()

        frame_0 = tk.Frame(self.des, bg="#e8ded2")
        tk.Label(frame_0, text='DES', font=('Calibri', 16), bg='#DC143C').pack(side='left', pady=6)
        tk.Label(frame_0, text='Data Encryption', font=('Calibri', 16), bg="#e8ded2").pack(side='left', padx=6, pady=6)

        btn_back = tk.Button(frame_0, text='TO DECRYPTION', font=('Calibri', 14), bg='#DC143C', command=self.change,
                             pady=6)
        btn_back.pack()
        frame_0.pack(side='top')

        # frame1
        frame_1 = tk.Frame(self.des, bg="#e8ded2")
        frame_1_top = tk.Frame(frame_1, bg="#e8ded2")
        frame_1_bottom = tk.Frame(frame_1, bg="#e8ded2")
        tk.Label(frame_1_top, text='Plaintext', font=('Arial', 14), bg='#F0E68C', bd=2, relief='flat').pack(side='left')

        self.plaintext = tk.Text(frame_1_bottom,
                                 font=('Arial', 12),
                                 height=6,
                                 bg='#89c9b8',
                                 relief='solid',
                                 bd=2,
                                 width=40,
                                 padx=1,
                                 pady=1,
                                 state='normal',
                                 cursor='arrow',
                                 wrap='char',
                                 )
        self.plaintext.pack()

        frame_1_top.pack(side='top')
        frame_1_bottom.pack(side='bottom')
        frame_1.pack(side='top', expand='yes', fill='x', pady=20)

        keyVar = tk.StringVar()
        frame_2_top = tk.Frame(self.des, bg="#"
                                            "e8ded2")
        tk.Label(frame_2_top, text='Key',
                 font=('Arial', 14), bg="#"
                                        "e8ded2"
                 ).pack(side='left', pady=10)

        self.Key = tk.Entry(frame_2_top, bg='#ff8e6e', textvariable=keyVar, width=30, font=('Arial', 12),
                            relief='solid',
                            bd=2)
        self.Key.pack(side='left')
        frame_2_top.pack(side='top')

        # frame2
        frame_2 = tk.Frame(self.des, bg="#e8ded2")
        tk.Button(frame_2, text='Encipher', command=self.encrypt, bg='#318fb5', width=10, font=('Arial', 14)).pack(
            side='bottom', padx=50, pady=10)

        frame_2.pack(side='top')
        frame_2.pack(side='top', expand='yes', pady=10)

        # frame3
        frame_3 = tk.Frame(self.des, bg="#"
                                        "e8ded2")
        frame_3_top = tk.Frame(frame_3, bg="#"
                                           "e8ded2")
        frame_3_bottom = tk.Frame(frame_3, bg="#"
                                              "e8ded2")
        tk.Label(frame_3_top, text='Secret Text', font=('Arial', 14), bg="#F0E68C").pack(side='left')
        self.secret = tk.Text(frame_3_bottom,
                              font=('Arial', 12),
                              height=6,
                              bg='#89c9b8',
                              fg='red',
                              relief='solid',
                              bd=2,
                              width=40,
                              padx=1,
                              pady=1,
                              state='normal',
                              cursor='arrow',
                              wrap='char',
                              )
        self.secret.pack()
        frame_3_top.pack(side='top')
        frame_3_bottom.pack(side='bottom')
        frame_3.pack(side='top', expand='yes', fill='x', pady=40)

    def encrypt(self, ):
        self.secret.config(fg='red')
        self.plaintext.config(fg='black')
        text = self.plaintext.get('0.0', 'end').strip()
        key = self.Key.get().strip()
        result = encryption(input_text=text, input_key=key, optionType=0)
        self.secret.delete('1.0', 'end')
        self.secret.insert('end', result)

    def change(self, ):
        self.des.destroy()
        DES_decryption(self.master)


class DES_decryption():
    def __init__(self, master):
        self.master = master
        self.master.config()
        self.des = tk.Frame(self.master, bg="#e8ded2")
        self.des.pack()

        frame_0 = tk.Frame(self.des, bg="#e8ded2")
        tk.Label(frame_0, text='DES', font=('Calibri', 16), bg='#DC143C').pack(side='left', pady=6)
        tk.Label(frame_0, text='Data Encryption', font=('Calibri', 16), bg="#e8ded2").pack(side='left', padx=6, pady=6)

        btn_back = tk.Button(frame_0, text='TO ENCRYPTION', font=('Calibri', 14), bg='#DC143C', command=self.change,
                             pady=6)
        btn_back.pack()
        frame_0.pack(side='top')

        # frame1
        frame_1 = tk.Frame(self.des, bg="#e8ded2")
        frame_1_top = tk.Frame(frame_1, bg="#e8ded2")
        frame_1_bottom = tk.Frame(frame_1, bg="#e8ded2")
        tk.Label(frame_1_top, text='Secret Text', font=('Arial', 14), bg='#F0E68C', bd=2, relief='flat').pack(
            side='left')

        self.plaintext = tk.Text(frame_1_bottom,
                                 font=('Arial', 12),
                                 height=6,
                                 bg='#89c9b8',
                                 relief='solid',
                                 bd=2,
                                 width=40,
                                 padx=1,
                                 pady=1,
                                 state='normal',
                                 cursor='arrow',
                                 wrap='char',
                                 )
        self.plaintext.pack()

        frame_1_top.pack(side='top')
        frame_1_bottom.pack(side='bottom')
        frame_1.pack(side='top', expand='yes', fill='x', pady=20)

        keyVar = tk.StringVar()
        frame_2_top = tk.Frame(self.des, bg="#"
                                            "e8ded2")
        tk.Label(frame_2_top, text='Key',
                 font=('Arial', 14), bg="#"
                                        "e8ded2"
                 ).pack(side='left', pady=10)

        self.Key = tk.Entry(frame_2_top, bg='#ff8e6e', textvariable=keyVar, width=30, font=('Arial', 12),
                            relief='solid',
                            bd=2)
        self.Key.pack(side='left')
        frame_2_top.pack(side='top')

        # frame2
        frame_2 = tk.Frame(self.des, bg="#e8ded2")
        tk.Button(frame_2, text='Decipher', command=self.decrypt, bg='#318fb5', width=10, font=('Arial', 14)).pack(
            side='bottom', padx=50, pady=10)

        frame_2.pack(side='top')
        frame_2.pack(side='top', expand='yes', pady=10)

        # frame3
        frame_3 = tk.Frame(self.des, bg="#"
                                        "e8ded2")
        frame_3_top = tk.Frame(frame_3, bg="#"
                                           "e8ded2")
        frame_3_bottom = tk.Frame(frame_3, bg="#"
                                              "e8ded2")
        tk.Label(frame_3_top, text='Plaintext', font=('Arial', 14), bg="#F0E68C").pack(side='left')
        self.secret = tk.Text(frame_3_bottom,
                              font=('Arial', 12),
                              height=6,
                              bg='#89c9b8',
                              fg='red',
                              relief='solid',
                              bd=2,
                              width=40,
                              padx=1,
                              pady=1,
                              state='normal',
                              cursor='arrow',
                              wrap='char',
                              )
        self.secret.pack()
        frame_3_top.pack(side='top')
        frame_3_bottom.pack(side='bottom')
        frame_3.pack(side='top', expand='yes', fill='x', pady=40)

    def decrypt(self, ):
        self.secret.config(fg='red')
        self.plaintext.config(fg='black')
        text = self.plaintext.get('0.0', 'end').strip()
        key = self.Key.get().strip()
        result = decryption(input_text=text, input_key=key, optionType=1)
        self.secret.delete('1.0', 'end')
        self.secret.insert('end', result)

    def change(self):
        self.des.destroy()
        DES_encryption(self.master)


if __name__ == '__main__':
    root = tk.Tk()
    base(root)
    root.mainloop()
