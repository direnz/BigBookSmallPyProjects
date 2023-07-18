"""Caesar Cipher Hacker, by Al Sweigart al@inventwithpython
This program hacks messages encrypted with the Caesar cipher by doing
a brute force attack against every possible key.    
More info at: https://en.wikipedia.org/wiki/Caesar_cipher
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner, cryptography, math"""

print('Caesar Cipher Hacker, by Al Sweigart')

# Let the user specify the message to hack:
print('Enter the encrypted Caesar cipher message to hack.')
message = input('> ')

# Every possible symbol that can be encrypted/decrypted:
# (This must match the SYMBOLS used when encrypting the message.)   
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Loop through every possible key: 
for key in range(len(SYMBOLS)):