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