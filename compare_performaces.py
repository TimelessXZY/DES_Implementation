from tkinter import messagebox

import DES_algorithm
import RSA_algorithm
import time
import tkinter as tk
from tkinter.constants import END

class CopmareGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("RSA & DES Encryption and Decryption Comparison")
        self.geometry("800x600")
        self.setup_ui()

        self.correct_pbk = None
        self.correct_pvk = None
        self.plainText_length = None

    def setup_ui(self):
        # Text Entry (plain text)
        self.label1 = tk.Label(self, text="Enter Plain Text:")
        self.label1.pack()
        self.text_entry1 = tk.Entry(self, width=50)
        self.text_entry1.pack()
        # Text Entry (encrypted text)
        self.label2 = tk.Label(self, text="Enter Encrypted Text:")
        self.label2.pack()
        self.text_entry2 = tk.Entry(self, width=50)
        self.text_entry2.pack()
        # input key
        self.label3 = tk.Label(self, text="Enter Key:")
        self.label3.pack()
        self.text_entry3 = tk.Entry(self, width=50)
        self.text_entry3.pack()
        # rsa encrypt button
        self.rsa_encrypt_button = tk.Button(self, text="RSA Encrypt", command=self.rsa_encrypt_text, font=('Arial', 14), bg="#e8ded2")
        self.rsa_encrypt_button.pack()
        # rsa decrypt button
        self.rsa_decrypt_button = tk.Button(self, text="RSA Decrypt", command=self.rsa_decrypt_text, font=('Arial', 14), bg="#e8ded2")
        self.rsa_decrypt_button.pack()
        # des decrypt button
        self.des_decrypt_button = tk.Button(self, text="DES Encrypt", command=self.des_encrypt_text, font=('Calibri', 14), bg='#DC143C')
        self.des_decrypt_button.pack()
        # des decrypt button
        self.des_decrypt_button = tk.Button(self, text="DES Decrypt", command=self.des_decrypt_text, font=('Calibri', 14), bg='#DC143C')
        self.des_decrypt_button.pack()
        # output encrypted text
        self.label4 = tk.Label(self, text="RSA Encrypted / Decrypted Text:", font=('Arial', 14))
        self.label4.pack()
        self.text_entry4 = tk.Entry(self, width=50)
        self.text_entry4.pack()
        # output key
        self.label5 = tk.Label(self, text="RSA Private Key:", font=('Arial', 14))
        self.label5.pack()
        self.text_entry5 = tk.Entry(self, width=50)
        self.text_entry5.pack()
        # output encrypted text
        self.label6 = tk.Label(self, text="DES Encrypted / Decrypted Text:", font=('Calibri', 14))
        self.label6.pack()
        self.text_entry6 = tk.Entry(self, width=50)
        self.text_entry6.pack()

    def rsa_encrypt_text(self):
        plain_text = self.text_entry1.get()
        self.plainText_length = len(plain_text)
        if plain_text:
            start_time = time.process_time()
            upper = 100
            public_key, private_key = RSA_algorithm.generate_rsa_keys(upper)
            encrypted_text = RSA_algorithm.encrypt(plain_text, public_key)
            end_time = time.process_time()
            self.correct_pbk = public_key
            self.correct_pvk = private_key
            messagebox.showinfo(message='RSA Encoded successfully!\n'
                                        '{}s spent.'.format(end_time - start_time))
            print("The length ", self.plainText_length, " of text are encrypted spending ", end_time - start_time)
            self.text_entry4.delete(0, END)
            self.text_entry4.insert('end', encrypted_text)
            self.text_entry5.delete(0, END)
            self.text_entry5.insert('end', private_key)
        else:
            messagebox.showerror("Error", "Please enter text to encrypt.")

    def rsa_decrypt_text(self):
        encrypted_text = self.text_entry2.get()
        input_key = self.text_entry3.get()
        if encrypted_text:
            start_time = time.process_time()
            input_key = input_key.split()
            input_key = (int(input_key[0]), int(input_key[1]))
            decrypted_text = RSA_algorithm.decrypt(encrypted_text, input_key, self.correct_pvk)
            end_time = time.process_time()
            self.text_entry4.delete(0, END)
            self.text_entry4.insert('end', decrypted_text)
            messagebox.showinfo(message='RSA Decoded successfully!\n'
                                        '{}s spent.'.format(end_time - start_time))
            print("The length ", self.plainText_length, " of text are decrypted spending ", end_time - start_time)
        else:
            messagebox.showerror("Error", "Please enter text to decrypt.")


    def des_encrypt_text(self):
        start_time = time.process_time()
        text = self.text_entry1.get()
        key = self.text_entry3.get()
        result = DES_algorithm.encryption(input_text=text, input_key=key, optionType=0)
        end_time = time.process_time()
        self.text_entry6.delete(0, END)
        self.text_entry6.insert('end', result)
        messagebox.showinfo(message='DES Encoded successfully!\n'
                                    '{}s spent.'.format(end_time - start_time))
        print("The length ", self.plainText_length, " of text are encrypted spending ", end_time - start_time)


    def des_decrypt_text(self):
        start_time = time.process_time()
        text = self.text_entry2.get()
        key = self.text_entry3.get()
        result = DES_algorithm.decryption(input_text=text, input_key=key, optionType=1)
        end_time = time.process_time()
        self.text_entry6.delete(0, END)
        self.text_entry6.insert('end', result)
        messagebox.showinfo(message='DES Decoded successfully!\n'
                                    '{}s spent.'.format(end_time - start_time))
        print("The text are decrypted spending ", end_time - start_time)

if __name__ == '__main__':
    app = CopmareGUI()
    app.mainloop()

    # 10: helloworld
    # 20: somebodyknowasdsdffd
    # 30: sdasdddddwwewqwdsdasdsdsdwqwdw
    # 40: Idonknowifyouarethetrueloveformeoryouare
    # 50: somethingyoudontunderstandaretherealthingssmakemes

