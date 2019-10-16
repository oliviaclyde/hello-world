# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
# and makes a new list of only the first and last elements of the given list. 


a = [5, 10, 15, 20, 25]

newList = []

def listOfNum():
    newList.append(a[0])
    newList.append(a[len(a)-1])



listOfNum()
print(newList)

