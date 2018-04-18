import random
import sys
import os

# Tuples

# to create a tuple object
pi_tuple = (3,1,4,1,5,9)

print("PI_TUPLE: ", end="")
print(pi_tuple)

# convert a tuple into a List
new_list = list(pi_tuple)

print("NEW_LIST: ", end="")
print(new_list)

# convert a list into a tuple
new_tuple = tuple(new_list)

# length of tuple
leng = len(pi_tuple)

print("LENGTH: %s" %  (leng))

# max of tuple
max = max(pi_tuple)

print("MAX: %s" % (max))

# mih of tuple
min = min(pi_tuple)

print("MIN: %s" % (min))
