import math
import random
import tkinter as tk
import binascii
import re


# ===================== Tool Functions =====================
# This function is used to determine whether a number is prime
def isPrime(num):
    value = math.sqrt(num)
    for i in range(2, int(value) + 1):
        if num % i == 0:
            return False
        else:
            continue
    return True


# This function is used to find the greatest common divisor (GCD) between num1 and num2
def find_GCD(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1


# This function is used to find modular inverse using extended Euclidean algorithm
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1


# This function is used to generate large prime numbers for RSA key generation
def generate_prime(upper):
    while True:
        num = random.choice(range(upper))
        if isPrime(num):
            return num


# This is Key generation function
def generate_rsa_keys(upper):
    prime_p = generate_prime(upper)
    prime_q = generate_prime(upper)
    n = prime_p * prime_q
    phi = (prime_p - 1) * (prime_q - 1)
    public_exponent = random.randint(2, phi - 1)
    while find_GCD(public_exponent, phi) != 1:
        public_exponent = random.randint(2, phi - 1)
    private_exponent = mod_inverse(public_exponent, phi)
    return ((public_exponent, n), (private_exponent, n))


# This function is used to decode hex text
def change_to_str(hex_text):
    output_text = ''
    c = ''
    for i in hex_text.split():
        value = hex(int(i))[2:]
        # If it is not an even length, fill in zero at the beginning
        if len(value) == 1:
            value = '0' + value
        c += value
    i = 0
    while i < len(c):
        # Determine whether it is a Chinese character (read six characters at a time)
        # or a non-Chinese character (two characters)
        try:
            s = binascii.unhexlify(c[i:i + 6]).decode('utf-8')
            i += 6
        except UnicodeDecodeError:
            s = binascii.unhexlify(c[i:i + 2]).decode('utf-8')
            i += 2
        output_text += s
    return output_text


# ===================== Encryption and Decryption =====================
def encrypt(plain_text, public_key):
    hex_value = plain_text.encode('utf-8').hex()
    hex_chunks = re.findall(r'.{2}', hex_value)
    encrypted_message = ''

    for chunk in hex_chunks:
        tex = int(chunk, 16)
        value = str(pow(tex, public_key[0]) % public_key[1])
        for a in range(0, 4 - len(value)):
            value = '0' + value
        encrypted_message += value

    return encrypted_message


def decrypt(encrypted_text, private_key):
    decrypted_text = ''
    encrypted_chunks = re.findall(r'.{4}', encrypted_text)

    for chunk in encrypted_chunks:
        tex = int(chunk)
        decrypted_chunk = str(pow(tex, private_key[0]) % private_key[1]).zfill(4)
        decrypted_text += decrypted_chunk
        decrypted_text += ' '

    decrypted_text = change_to_str(decrypted_text)
    return decrypted_text


if __name__ == '__main__':
    # bits = 10  # Key size, you can increase it for more security
    # message = "什么东西啊!"
    # encrypted_message, pbk, pvk = rsa_encrypt(message, bits)
    # print("Encrypted Message:", encrypted_message)
    # print("Public Key: ", pbk)
    # print("Private Key: ", pvk)
    # decrypted_message = rsa_decrypt(encrypted_message, pvk)
    # print("Decrypted Message:", decrypted_message)

    upper = 100  # Key size, you can increase it for more security
    message = "sorry no!"
    pbk, pvk = generate_rsa_keys(upper)
    encrypted_message = encrypt(message, pbk)
    print("Encrypted Message:", encrypted_message)
    print("Public Key: ", pbk)
    print("Private Key: ", pvk)
    decrypted_message = decrypt(encrypted_message, pvk)
    print("Decrypted Message:", decrypted_message)


