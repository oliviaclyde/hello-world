# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

list = [5, 6, 2, 9, 7, 0, 1, 3, 4, 8, 11, 13, 15, 19, 14, 16, 12, 18, 17]

# Sort list
list.sort()

# Iterate and see if number at [i+1] is one more than i
def findMissingNumber():

    for i in list:
        for j in list:
            j = (i + 1)
            if list[j] - list[i] == 1:
                continue
            else: 
                return((list[j] + list[i])/2)
                break


print(findMissingNumber())

