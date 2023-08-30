"""Collatz Sequence, by Al Sweigart al@inventwithpython.com
Generates numbers for the Collatz sequence, given a starting number.
More info at: https://en.wikipedia.org/wiki/Collatz_conjecture
View this code at: https://nostartch.com/big-book/small-python-projects
Tags: tiny, beginner, math"""

import sys, time

print('''Collatz Sequence, or, the 3n + 1 Problem
      by Al Sweigart al@inventwithpython.com
      
      The Collatz sequence is a sequence of numbers produced from a starting number n, following three rules:
      
      1) If n is even, the next number n is n / 2.
      2) If n is odd, the next number n is n * 3 + 1.
      3) If n is 1, stop. Otherwise, repeat.
      
      it is generally thought, but so far not mathematically proven, that every starting number eventually terminates at 1.''')

