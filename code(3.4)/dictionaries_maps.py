import random
import sys
import os

# Dictionaries/Maps

# Dictionaries have a unique key for each value that will be store
# similar to lists, but you cannot join dictionaries together so easily like a list can be

# here we will create a list
#                                 KEY : VALUE
presidents_dictionary = {'Republican' : 'George W. Bush',
                            'Democrat' : 'Barack Obama',
                            'Crazy' : 'Donald J. Trump',
                            'Possible Future Presidents' : 'Oprah Winfrey',
                            'Possible Future Presidents1' : 'Dwayne Johnson'}

# We can print out by specific KEY
print(presidents_dictionary['Crazy'])

# we can delete a value by it's KEY
del(presidents_dictionary['Possible Future Presidents'])

# we can change the value for a specific KEY
presidents_dictionary['Possible Future Presidents1'] = 'James Patterson'

# Lets see how it prints the dictionary
print(presidents_dictionary)

# we can find the length easily
print(len(presidents_dictionary))

# find the value using the KEY again
print(presidents_dictionary.get("Democrat"))

# we can print the KEYS easily
print(presidents_dictionary.keys(), end="")

print(" \n ")

# we cam also print the VALUES easily
print(presidents_dictionary.values())
