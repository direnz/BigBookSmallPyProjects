"""Blackjack, by Al Sweigart al@inventwithpython
The classic card game also known as 21. (This version doesn't have
splitting or insurance.)
More info at: https://en.wikipedia.org/wiki/Blackjack
View this code at https://nostarch.com/big-book-small-python-projects
Tags: large, game, card game"""

import random, sys

# Set up the constants:
HEARTS   = chr(9829) # Character 9829 is '♥'.
DIAMONDS = chr(9830) # Character 9830 is '♦'.
SPADES   = chr(9824) # Character 9824 is '♠'.
CLUBS    = chr(9827) # Character 9827 is '♣'.
# (A list of chr codes is at https://inventwithpython.com/charactermap)
BACKSIDE = 'backside'

