people = 30
cars = 40
trucks = 15

#If this if statement evaulates true, the block of code will run
if cars > people:
    print("We should take the cars.")
#Otherwise if this is true, this block of code will run
elif cars < people:
    print("We should not take the cars.")
#If both are false, this code will execute
else:
    print("We can't decide.")

#If this statement is true, the block of code will run
if trucks > cars:
    print("That's too many trucks.")
#Otherwise if this is true, the block of code will run
elif trucks < cars:
    print("Maybe we could take the trucks.")
#If both of the prior are false, this code will execute
else:
    print("We still can't decide.")

#If this statement is true, the block of code will run
if people > trucks:
    print("Alright, let's just take the trucks.")
#If the above is false, this code will execute
else:
    print("Fine, let's stay home then.")

#Trying more complex boolean expressions
if people < cars or trucks > cars:
    print("Let us walk!")

if people > cars and trucks < cars:
    print("Give us a ride!")
elif trucks == cars:
    print("Going for a ride!")
else:
    print("We made it!")
