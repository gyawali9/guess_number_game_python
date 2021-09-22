#!/usr/bin/env python
# coding: utf-8

# # Number Guessing Game

# In[1]:


print("Welcome to number guessing game")
print("        ***********            ")

guess = input("Please guess a number between 1 to 10.")

import random
random_number = random.randint(1,10)

def guess_game(g, r):
    if g == r:
         print("Congratulation!!! You have guessed correct number" + str(g))
    else:
        print("Sorry! Incorrect guess => " + str(g) + "." + " Correct number is " + str(random_number) + ".")

guess_game(guess, random_number)

