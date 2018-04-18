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
