ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ') #splits the long string into separate items in a list
more_stuff = ["Day", "Night", "Song", "Frisbee",
                "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) #whoa! fancy #starts at the end of the list
print(stuff.pop()) #starts at the end of this list
print(' '.join(stuff)) #what? cool! #Combines items into a long string instead of objects in a list
print('#'.join(stuff[3:5])) # spuer stellar! #combines the 3rd item and the 4th item (stops before 5)
