import random
import sys
import os

# Lists

# to create a list use [] like an array but not
name_list = ['James', 'Earl', 'Patterson']

# Lets print out the values for each one of the entries
print(name_list[0] + " " + name_list[1] + " " + name_list[2] + " ")

# you could just print off one individual entry
print(name_list[0] + " said it was okay to program in python 3.4, mate.")

# Let's say I want to print from an index to another index (but not including that last index)
print(name_list[0:3])

# We can have a list of lists
# Let's create two lists
abc_list = ['a', 'b', 'c']
def_list = ['d', 'e', 'f']

# now create a list, and store the two lists inside of our list
abcdef = [abc_list, def_list]

# let's print our list
print(abcdef)

# lets say we want the 3rd item of the 2nd list
# It is set up like a multidimensional array would be
print(abcdef[1][2])

print(abcdef)

# another list
ghi = ['g','h','i']

# Let us append another list to our list of lists
abcdef.append(ghi)

# Now lets add on to our list ghi we just created
ghi.append('j')

print(ghi)

print(abcdef)

# I could add to a specific index of a list
ghi.insert(4, 'k')

print(ghi)

print(abcdef)

# and I could very easily remove from specific indexes
ghi.remove('k')

ghi.remove('j')

print(ghi)

print(abcdef)

# I could sort the items easily, inreverse order as well
# reverse first, since they are already in order
ghi.reverse()

print(ghi)

print(abcdef)

# Now sort the list in alphabetical order
ghi.sort()

print(ghi)

print(abcdef)

# And now let's delete the 2nd index of our abcdef list since ghi doesn't fit in anyway
del abcdef[2]

print(abcdef)

# we can combined lists together into one longer list
com_list = abc_list + def_list

print(com_list)

# length
print(len(com_list))

# maximum (strings : highest alphabetically)
print(max(com_list))

# minimum (strings : lowest alphabetically)
print(min(com_list))
