#Practice Python
#Exercise 1
#Character Input
#Create a program that asks the user to enter their name and their age.
#Print out a message addressed to them that tells them the year that they will turn 100 years old.

user = input("Please enter your name: ")
age = int(input("Enter your age: "))
incremental_years = 100 - age
year = 2019
year_centurian = str(year + incremental_years)
print(user + " will be 100 years old in the year " + year_centurian)
