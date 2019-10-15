# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

# Extras:
#1. Write two different functions to do this - one using a loop and constructing a list, and another using sets.


# Using sets - makes them naturally ordered
a = [4, 7, 1, 9, 5, 2, 7, 4]

b = []

def noDups():
    # b = []
    # set_b = set(b)
    set_a = set(a)
    set_b = set(b)
    set_a.update(set_b)
    print(set_a)


noDups()


# Extra #1 - using dictionary - existing order preserved

a = [4, 7, 1, 9, 5, 2, 7, 4]

aNew = list(dict.fromkeys(a))
print(aNew)

# Extra #1 - using loop

a = [4, 7, 1, 9, 5, 2, 7, 4]

b = []

for i in range(len(a)):
    if a[i] not in b:
        b.append(a[i])
print(b)


# Extra #2 - try comparing two lists and not including dups (using loops and not sets)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = []

# Would need to know which list is longer
# for i in a:
#     for n in b:
#         if i == n:
#             continue
#         else: 
#             # Can't get this piece to work
#             c.append[a(i)]
#             c.append[b(i)]
            
# print(c)
