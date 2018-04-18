import random
import sys
import os

# File Input/Output

# create/open a file ("name.ext", "file_mode")
# wb to write to the file
# ab+ to read & append a file, also opens/creates the file
test_file = open("tutorial.txt", "wb")

# print out the file_mode that is being used
print(test_file.mode)

# print out the name
print(test_file.name)

# this is how you write text to the file
# technically, this is how to write in bytes to a file
test_file.write(bytes("This is how you write to a file using Python\n", 'UTF-8'))

test_file.close()

# The file will be created within the same directory as the current py file is being stored
# So, if you have this py file saved to your desktop, the file created will be stored on the desktop

# Let's take a look at how to open and read the file

# we open the file with reading and writing priviledges
test_file = open("tutorial.txt", "r+")

# we store the contents of the file being read into a variable named test_in_file
test_in_file = test_file.read()

# print the variable
print(test_in_file)

# to delete the file
os.remove("tutorial.txt")

# more on File Input Output soon
