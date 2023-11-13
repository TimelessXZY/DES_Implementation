# DES_Implementation
This is the project 1 & 2 of course Security & Privacy.

# Basic Functionalities
1. No restriction to the length of plain text and keys.
2. Beautiful user interface
3. Encryption & Decryption are two independent components
4. RSA encryption and decryption implemented
5. Performances comparison between DES and RSA

# Script for project 1
Hello, professors. In this video, I will briefly show my implementation of DES algorithm and the basic operation guidelines of my project.

First of all, in this file, there are four main parts of DES. 
The first part is operation tables. 
The second part is type conversion, which includes the char-unicode conversion, unicode-bit and byte-bit conversions. 
The third part is DES algorithm which implements in DES_pipeline and generate_keys functions.
The fourth part is user interface which includes classes of windows and components.

Next I will briefly show the guidelines of operation. 
In this encryption component, click the button TO DECRYPTION at the right upper corner will turn to the decryption component 
and click the button TO ENCRYPTION will turn to the encryption component again. 
In encryption component, type plain text and key in the frames
and then click the encipher button will get the encrypted text in the frame below. The decryption processes are similar.

That's much of it. Thanks for watching.

# Script for project 2
Hello, professors. In this video, I will briefly show my implementation of project 2, 
which includes both the implementation of DES and RSA algorithm and performances comparison between these two algorithms.

First of all, in DES_algorithm file, I achieve the DES algorithm. Users can run this file to use DES encryption and decryption.

Second, in RSA_algorithm file, I implement the main functions of RSA algorithm, 
such as prime number generation, calculation of Euler's totient function, and modular exponentiation as well as the public key
and private key generation, corresponding encryption and decryption. Users can also run this file to use RSA encryption and 
decryption.

Third, in compare_performance file, I integrate two algorithms and create a user interface for user to interact, which enables
user to use both DES and RSA algorithms and show users the time spent on encryption or decryption. After running this file, 
user can enter the plain text or corresponding key and select algorithm to encrypt and later enter encrypted text and key to decrypt.

After encryption and decryption, the message related to the time spent on them will pop out. 

In the experiment, I found that the RSA has a better efficiency but is less security than DES due to the small size of prime numbers 
of p and q.

That's much of it. Thanks for watching.
