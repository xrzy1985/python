import random
import sys
import os

# functions

'''
Functions help us write reusable code, organize our code, and
generally keep our code looking more professional.
'''

# Here we define a function to add two numbers together
def addNum(n1, n2):
    sum = n1+n2
    return sum

# use our function within a print statement
print(addNum(5,1))

# or store the value inside of a string
string = str(addNum(6,2))
print(string)

# we do not have to have parameters at all in functions
def worth_less():
    str = "this does nothing but print"
    print(str)

worth_less()

# Functions can handle no parameters, to as many as you need
# you don't need to actually specify what data types each one
# will be since Python can interpret which one you want to use
# one important thing to remember about functions inside of Python
# is the idea of local scope vs global scope. For instance, the
# str variable above is a local variable only available inside
# the scope of worth_less. 
