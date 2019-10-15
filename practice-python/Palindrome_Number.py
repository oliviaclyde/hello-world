# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

# Example 1:

# Input: 121
# Output: true

# Remember to convert the int to a str so you can compare if they are equal
num = str(input("Please enter a number, and I will tell you if that number is a palindrome (the same forwards and backwards): "))

newNum = str(num)[::-1]

if num == newNum:
    print("The number is a palindrome.")
else:
    print("The number is NOT a palindrome.")