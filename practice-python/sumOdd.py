# Write a function that takes a list of ints as an arg
# Function should return an int that is the sum of any odd numbers


def sumOddNumbers (numbers):
    total = 0
    for item in numbers:
        if item % 2 != 0:
            total += item

    print(total)


sumOddNumbers([1,2,3,4,5,7])
