import random
import sys
import os

# While loops

# while loops are useful if you don't know how many times you
# need to actually loop through the while loop block

# this will create a variable with a random number between 1 and 100
r_num = random.randrange(0, 101)

cnt = 1

# while(condition)
while(r_num != 100):
    print(r_num)
    # we need to generate another random number
    # or we will be stuck in a infinite loop
    # unless we happen to get a 100 on the spot
    r_num = random.randrange(0, 101)
    # lets count how many times it actually loops through
    # increment cnt
    cnt+=1

print("We have looped " + str(cnt) + " times so far to reach " + str(r_num) + ".")

i = 0

# The code below will print out the even numbers until i is greater than 9
# once that happens, the code will break out of the loop until the loop is finished
while( i <= 20):
    if(i%2 == 0):
        print(i)
    elif(i == 9):
        # remember, break will break out of the current block
        # no even numbers will print past 8
        break
    else:
        i += 1  # remember, i++
        # continue will skip the rest of the block
        # and continue at the top of the block again
        continue

    i += 1
