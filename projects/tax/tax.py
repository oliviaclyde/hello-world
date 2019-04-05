#This will calculate how much tax you owe and what your refund will be
print("Welcome to the tax calculator!")
gross = input("What was your gross annual income for 2018? ") #Need to make this integer only
marital_status = input("What is your marial status? ")
if marital_status == "m" or marital_status == "married":
    print("Accepted")
elif marital_status == "s" or marital_status == "single":
    print("Accepted")
else:
    print("Error. Please try again.") #Need to loop this be for re-input someehow
withholding = input("What is your total federal withholding? ")


#Tax rates
#Single
#Married
#Calculate the tax burden
#Calculate refund/owing
