import random
import sys
import os

# Logical Operators

'''

    AND -> and
    OR  -> or
    NOT -> !

'''

# create a variable with a random age
age = 54

# lets create a boolean to be True or False
driving_test = True

if (age < 15) :
    print("You can drive a power wheel, mate.")
# age must be greater or = to 16 or less than 65
# and the driving_test results must be True
# redundant, but you can use not(condition) to negate a condition
# it is saying driving test must equal True
elif (age >= 16 and age <= 65 and driving_test == True and not(driving_test == False)) :
    print("You are old enough to drive, mate.")
# here we are using the or logical operator to say
# the age must be greater than 65 or your driving test results do not equal True
elif (age > 65 or driving_test != True) :
    print("You are too old to drive, mate.")
else:
    print('You absolutely cannot drive, mate.')
