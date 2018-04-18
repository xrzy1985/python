import random
import sys
import os

# Arithmetic
'''

Addition : +
Subtraction : -
Multiplication : *
Division : /
Modulus : %
Exponential  : **
Floor Division : // (division then discard remainder and rotate down)
                    14.5 would be changed to 14

'''

print("5 + 2 = ", 5+2)      # 7
print("5 - 2 = ", 5-2)      # 3
print("5 * 2 = ", 5*2)      # 10
print("5 / 2 = ", 5/2)      # 2.5
print("5 % 2 = ", 5%2)      # 1
print("5 ** 2 = ", 5**2)    # 25
print("5 // 2 = ", 5//2)    # 2

# When performing arithmetic in any programming language you need to remember
# ORDER OF OPERATION MATTERS

# the code below will read the line, and do the arithmetic from left to right
print("1 + 2 - 3 * 2 = ", 1+2-3*2)      # -3

# The following will have completely different results than the code above
print("(1 + 2 - 3) * 2 = ", (1+2-3)*2)  # 0
