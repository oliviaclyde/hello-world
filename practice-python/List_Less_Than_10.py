# Write a program that prints out all the elements of the list that are less than 5.

# Extras:

# 1.Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
# 2. Write this in one line of Python.
# 3. Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.



a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in a:
    if i < 5:
        print(i)


# Extra #1

newList = []
for i in a:
    if i < 5:
        newList.append(i)

print(newList)

#Extra #2

#Can't quite do it in 1 line of code. This just prints tht same list. Need to figure out how only print < 5
for i in a < 5: newList.append(i)
print(newList)




#Extra #3

newList = []
num = int(input("Please enter a number: "))
for i in a:
    if i < num:
        newList.append(i)

print(newList)