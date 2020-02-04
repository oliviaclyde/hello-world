# Read csv file to console

import csv

with open('test.txt', 'r') as my_file:
    words = my_file.read()

    print(words)




# Read file and count how many times the same word appears

file = open('test.txt', 'r')

from collections import Counter
wordCount = Counter(file.read().split())

for item in wordCount.items(): 
    # the {} are formatters and items is put inside the brackets
    print("{}\t{}".format(*item))




# Read file and count how many are in each category

from collections import Counter

def main():
    with open('test2.txt') as file:
        for line in file:
            line = line.split("/")[2]
            print(line)
    
main()

# while line:
#     categoryCount = Counter(line)

#     for item in categoryCount.items():
#         print("{}\t{}".format(*item))
