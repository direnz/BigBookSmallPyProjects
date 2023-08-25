"""Cho-Han, by Al Sweigart al@inventwithpython.com
The traditional Japanese dice game of even-odd. 
view this code at https://nostarch.com/big-book-small-python-projects
Tags: short, beginner, game"""

import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN', 4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-Han, by Al Sweigart al@inventwithpython.com
      
      The traditional Japanese dice game, two dice are rolled in a bamboo
      cup by the dealer sitting on the floor. The player must guess if the dice total to an even (cho) or odd (han) number.''')

purse = 5000

while True:
    # Place your bet:
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        pot = input('> ')
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You don\'t have enough to make that bet.')
        else:
            #this is a valid bet. 
            pot = int(pot) #convert pot to an integer
            break #Exit the loop once a valid bet is placed. 

    # Roll the dice.