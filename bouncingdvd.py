"""Bouncing DVD Logo, by Al Sweigart al@inventwithpython.com
A bouncing DVD logo animation. You have to be "of a certain age" to
appreciate this. Press Ctrl-C to stop.

NOTE: Do not resize the terminal window while this program is running.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, artistic, bext, terminal"""

import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you can install by')
    print('following the instructions at https://pypi.org/project/Bext/')
    sys.exit()

