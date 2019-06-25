#Original Exercise
i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)


    i = i + 1
    print("Numbers now: ", numbers)
    print(f"As the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)


#Convert while-loop to a function, my code
i = 0
numbers = []

new_number = int(input("Enter a number: "))

def first(i):
    print(f"i is {i}")
    numbers.append(new_number)

    increment_number = int(input("Enter a number to increment by: "))
    i += increment_number
    numbers.append(i)
    print("Numbers now: ", numbers)

first(new_number)

print("The numbers: ")

for num in numbers:
    print(num)


Write the script using a for-loop and range


numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)
