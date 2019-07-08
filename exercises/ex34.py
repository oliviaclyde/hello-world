animals = ['bear', 'python3.6', 'peacock', 'kangaroo', 'whale', 'platypus']

#The animal at 1.
print("What animal is at 1?")
answer1 = input(">>  ")
if answer1 == animals[1]:
    print("That is correct.")
else:
    print("Sorry. Incorrect response.")

print("What animal is at 4?")
answer2 = input(">> ")
if answer2 == animals[4]:
    print("That is correct.")
else:
    print("Sorry. Incorrect response.")


print(animals[3])

for item in animals:
    print({item})
