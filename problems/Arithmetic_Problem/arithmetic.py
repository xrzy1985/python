import random
import sys
import os

if __name__ == '__main__':
    a = int(input())
    b = int(input())

    add = lambda a,b:a+b
    sub = lambda a,b:a-b
    mult = lambda a,b:a*b

    print(add(a,b))
    print(sub(a,b))
    print(mult(a,b))
