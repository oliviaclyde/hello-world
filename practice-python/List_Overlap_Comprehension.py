# Take two lists and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).

import random


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def inList(): 
    new_list = [item for item in a if item in b]
    
    for i in new_list:
        i = 0
        n = i + 1
        if new_list[i] == new_list[n]:
            new_list.pop(i)
            i+=1
          
    print(new_list)


inList()

# Now make the list generate random numbers

print("I'm going to generate a list of two random numbers. Then I will tell you what numbers are common between them.")

def randSample():
    a = random.sample(range(100), 13)
    b = random.sample(range(100), 7)

    common_numbers = [item for item in a if item in b]

    print(a)
    print(b)
    print("These are the common numbers between the two lists: ") 
    print(common_numbers)


randSample()