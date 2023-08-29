"""Clickbait Headline Generator, by Al Sweigart al@inventwithpython.com
A clickbait headline generator for your soulless content farm website.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: Large, beginner, humor word"""

import random

#setup the constants:
OBJECT_PRONOUNS = ['Her', 'Him', 'Them']
POSSESIVE_PRONOUNS = ['Her', 'His', 'Their']
PERSONAL_PRONOUNS = ['She', 'He', 'They']
STATES = ['California', 'Texas', 'Florida', 'New York', 'Pennsylvania','Illinois', 'Ohio', 'Georgia', 'North Carolina', 'Michigan']
NOUNS = ['Athlete', 'Clown', 'Shovel', 'Paleo Diet', 'Doctor', 'Parent','Cat', 'Dog', 'Chicken', 'Robot', 'Video Game', 'Avocado', 'Plastic Straw', 'Serial Killer', 'Telephone Psychic']
PLACES = ['House', 'Attic', 'Bank Deposit Box', 'School', 'Basement','Workplace', 'Donut Shop', 'Apocalypse Bunker']
WHEN = ['Soon', 'This Year', 'Later Today', 'RIGHT NOW', 'Next Week']

def main():