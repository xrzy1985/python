import random
import sys
import os

# if, else, and elif

# if statements are going to execute when a specific condition is met

'''

    Equal to     : ==
    Not Equal to : !=
    Great than   : >
    " or equal   : >=
    Less than    : <
    " or equal   : <=

'''

age = 15

if age >= 16 :
    print("You are old enough to drive, mate.")
else:
    print("You are not old enough to drive, mate.")

# spacing and indention are very important within Python
# if you do not have proper indention, your code might run, but could
# result in oddball results at given times

# Multiple conditions

age = 78

# we can define the conditions
if age < 16 :
    print("You can drive a power wheel, mate.")
# we can have multiple conditions
# remember && is and , || is or
elif (age >= 16 and age <= 65) :
    print("You are old enough to drive, mate.")
elif age > 65 :
    print("You are too old to drive, mate.")
#if no other conditions match, else will execute
# also, notice the use of single and double qoutation marks
# in Python, it does not matter
else:
    print('You absolutely cannot drive, mate.')
