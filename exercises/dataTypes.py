# list
myList = [1, 3, True, 6.5]
myList.append(4)
print(myList)
myList.insert(0, True)
print(myList)
myList.pop()
myList.pop(0)
print(myList)

newList = list(range(0,11))
print(newList)
newList.reverse()
print(newList)
newList.append(11)
print(newList)
newList.sort()
print(newList)

trickyList = [4, 7.3, "cat", True]
trickyList.reverse()
print(trickyList)
del trickyList[0]
print(trickyList)
print(trickyList.index('cat'))
trickyList.append('cat')
print(trickyList.count('cat'))
trickyList.remove(4)
print(trickyList)

# lists are mutable
trickyList[1] = 9
print(trickyList)

# create a list using range, then store in variable
list(range(10))
print(list(range(10)))
makeList = list(range(5,10,2))
print(makeList)
makeAnother = list(range(14,3,-4))
print(makeAnother)

# iterate over strings
myName = "David"
print(myName[3])
print(myName*2)
print(len(myName))
for i in myName:
    print(i)

for i in enumerate(myName):
    print([i])

for i in enumerate(myName):
    print(i)

# list of tuples
print(list(enumerate(myName)))
print(myName.upper())
print(myName.split('v'))

# strings are immutable
print(myName)
print(myName[1])
print(myName + "x")


# tuples
# immutable
myTuple = (2, True, 4.96, "cat", 6)
print(len(myTuple))
print(myTuple[1])
print(myTuple * 3)
print(myTuple[0:4])

# set
# unordered and NO duplicates
# mutable, can add items

mySet = {3, 6, "cat", 4.5, False}
print(mySet)
print(mySet)
print(mySet)
print(len(mySet))
print(False in mySet)
print("dog" in mySet)

secondSet = {7, 4, "dog", False, 2.1}
# returns all the items (excluding duplicates) from both sets
print(mySet | secondSet)
print(mySet.union(secondSet))

# returns a new set with only items in both sets
print(mySet & secondSet)
print(mySet.intersection(secondSet))

# returns a new set w/ all items from first set not in second set
print(mySet - secondSet)
print(secondSet - mySet)
print(mySet.difference(secondSet))

# asks if all elements in first set are in the second
print(mySet <= secondSet)
print(mySet.issubset(secondSet))

# add and remove items to your set 
mySet.add(5)
print(mySet)
mySet.remove("cat")
print(mySet)
mySet.pop()
print(mySet)
mySet.clear()
print(mySet)
mySet.add(2)
print(mySet)


# dictionary
# {'key':'value'} pair
myDict = {"Kelli": "Ray", "Christi": "Elliott", "Jami": "Ray", "Olivia": "Clyde"}

print(myDict.keys())
print(myDict.values())
print(myDict.items())
print(myDict.get("Olivia"))
print(myDict.get("Mel"))
print(myDict.get("Mel", "NO ENTRY"))
