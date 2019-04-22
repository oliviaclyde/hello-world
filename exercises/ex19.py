#Calling functions
#Defining a function and declaring two arguments

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"YOu have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

#Code skips above and comes to this print statement
print("We can just give the function numbers directly:")
#Now we are passing two arguments to the function and the code will go back and print the statement above
cheese_and_crackers(20, 30)

#Print statement
print("OR, we can use variables from our script:")
#Code skips past these two lines
amount_of_cheese = 30
amount_of_crackers = 50
#Code sees we have changed the arguments for this function and goes back two lines to call the function with new arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#Print statement
print("We can even do math inside too:")
#Code now re-runs function with new parameters, while solving the math inside the parameters
cheese_and_crackers(10 + 20, 5 + 6)

#Print statement
print("And we can combine the two, variables and math:")
#Code uses variable (which is an integar) and adds to it
cheese_and_crackers(amount_of_crackers + 100, amount_of_crackers + 1000)

#Now I'm creating my own function
def budget(save, spend):
    print(f"If you want to be successful with money, you must save {save} percent of your money.")
    print(f"If you spend {spend} percent you will run out of money.")

print("Running my function 10 different ways.")
print("1st")
budget(10, 100)

print("2nd")
rainy_day = 20
bills = 90
budget(rainy_day, bills)

print("3rd")
outflow = int(input("How much do you spend?"))
inflow = int(input("How much do you save?"))
budget(inflow, outflow)

print("4th")
outflow1 = int(input("Enter the % you spend monthly:"))
inflow1 = int(input("Enter the % you save monthly"))
budget(outflow1 + 15, inflow1 + 25)

print("5th")
budget(rainy_day - 5, bills + 5)

print("6th")
budget(outflow + outflow1, inflow + inflow1)

print("Shoot. Only could think up 6 different ways.")
