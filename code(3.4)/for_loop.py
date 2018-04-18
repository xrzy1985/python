import random
import sys
import os

# for loops

# lets create a for loop to print 1 to 10
for x in range(1, 11):
    print(x)

# Lets see a for loop cycle through a list
list = ['a', 'b', 'c', 'd', 'e', 'f']

for l in list:
    print(l)


# a list can be declared on the fly
for a in [3, 1, 4, 1, 5, 6]:
    print(a)

# Lets get a little fancy
# we create a list that has two indexes; (0) is a list of lists of numbers
# and (1) is a string of my hacker_tag
#        [  [ 0[  0  ], [  1  ], [  2  ]0 ] , [  1   ]   ]
n_list = [  [  [1,2,3], [4,5,6], [7,8,9]  ] , ["xRzy"]   ]

print(n_list)

# print the element in the 0 spot of the 1st index
print(n_list[1][0])

# we can do for loops inside for loops

abc_list = [['a','b','c'],['d','e','f'],['g','h','i']]

for x in range(0, 3):
    for y in range(0, 3):
        print(abc_list[x][y])


str_list = ["James", "Earl", "Patterson"]

for st in str_list:
    print(st)
