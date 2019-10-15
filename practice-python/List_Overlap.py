# Take two lists, say for example these two:

#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

# Extras:

#1. Randomly generate two lists to test this
#2. Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
a_set = set(a)
b_set = set(b)
common_elements = [i for i in a_set if i in b_set]
print(common_elements)


# Extra #1
import random

c = random.sample(range(1, 50), int(input("How many numbers in the first list would you like? "))) 
d = random.sample(range(1, 50), int(input("How many numbers in the second list would you like? ")))   
c_set = set(c)
d_set = set(d)

common_nums = [i for i in c_set if i in d_set]

# printing result 
print ("Random number list #1 is : " +  str(c))
print ("Random number list #2 is:" + str(d)) 
print(common_nums)


# Extra #2
# Can't write this in 1 line of python yet! Still need more practice