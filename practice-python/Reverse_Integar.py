# Given a 32-bit signed integer, reverse digits of an integer.

input = input("Please enter a number and I will reverse it: ")

# Change to a stringv in order to convert to a list. Once it's a list you can use the .reverse and .join properties
a = str(input)
b = list(a)
b.reverse()
a = "".join(b)
a = int(a)

print(a)