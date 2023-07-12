"""Caesar Cipher, by Al Sweigart al@inventiwtihpython
The Caesar cipher is a shift cipher that uses addition and subtraction
to encrypt and decrypt letters.
More info at: https://en.wikipedia.org/wiki/Caesar_cipher
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner, cryptography, math"""

try:
    import pyperclip #pyperclip copies text to the clipboard.
except ImportError:
    pass #if pyperclip is not installed, do nothing. It's no big deal.

#Every possible symbol that can be encrypted/decrypted:
# ( ! ) You can add numbers and punctuation marks to encrypt those as well.
#symbols as well. 
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('Caesar Cipher, by Al Sweigart')