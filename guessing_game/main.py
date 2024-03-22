#!python

import random

# Generates a computer guess between 1 and 5
com_num = random.randint(1, 5)

# Get an input from user
user_num=int(input("Please enter a number between 1 to 5: "))

# Print user's and computer's number
print(f"user:{user_num} and computer:{com_num}")

# Declare win or lose
if (user_num == com_num):
    print("You won!😀")
else:
    print("You lost.😒 Better luck next time!")
