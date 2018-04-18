import random
import sys
import os

# Strings
# You can use single or double qoutes

qoute = "Hello from the other side of the wherever, mate!"

# if you want to use a single or double qoute inside of your string
# use the backslash to let the
qoute2 = "Hello, I say, \"from the other side\""

print(qoute)

print(qoute2)

# You can store a string inside of a variable to use later on
name = "James Earl Patterson"
age = "30 years old"

print("I am " + name + " and I'm " + age + ".")

# you can set up strings to concatenate
str = "Please remember, you are unique "

multi_line_string_attachment = '''add the \'\'\' and then type
    as much as you'd like, on
    any line
    you
    want to type on. Just end the multiline string with \'\'\' at the end. '''

# print the strings out using the concatenation operator
print(str + multi_line_string_attachment)

# You can definitely format strings in Python
# it is different than Java, C#, C++, etc

print("I am %s and I'm %s." % (name, age))

# another way to add text
# %s will use the first variable/string you program into the parameters
# so, make sure you are setting the formatting correctly
print("%s I am %s and I'm %s." % ('Hello, ', name, age))

# to print off a new line, lets say, 5 new lines
print("\n" * 5)

# to not print off a newline every single time print is used
# the two print statements will be on the same line, but after right now, an end line will occur
print("I dont feel like using end line ", end="")
print("right now.")

# Lets say we want to find the 4th index of a string
long_string = "I'll run another 2 miles tomorrow morning"

# [starting_index:how_many_indeces]
print(long_string[0:4])

# Do you want to print the last word?
print(long_string[-7:])

# print everything up to the last word?
print(long_string[:-7])

print(long_string[:4] + " be there...")

# char string digit decimal with 5 places
print("%c - %s - %d - %.5f" % ('X', 'favorite', 1, .14))

# capitalize a string
st = "string"

# want to capitalize the first letter?
print(st.capitalize())

# Where is miles located?
print(long_string.find("miles"))

# check to see if string is all alphabets
print(long_string.isalpha())

# check to see if it is a number
print(long_string.isalnum())

# the length
print(len(long_string))

# replace a word with another
print(long_string.replace("miles", "kilometers"))

# to strip white space from a string
# long_string.strip()

# split string into a list
split_list = long_string.split(" ")

print(split_list)
