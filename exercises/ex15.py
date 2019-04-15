#Inport the sys module with the argument variable
from sys import argv
#We are now assigning 2 arguments to the variable
script, filename = argv
#Creating a new variable called "txt" and assigning it a function called "open"
#That function will then open the variable called "filename"
txt = open(filename)
#Print message using a format string f" { }"
print(f"Here's your file {filename}:")
#We are calling a function on the varable text
#Remember that we assigned the variable text above to open(filename)
#So now we are calling text and asking it to read
print(txt.read())

#Additional message printed
print("Type the filename again: ")
#This line is creating a new variable and assigning a user input prompt
#The program keeps moving down and will come back and execute this in a minute
file_again = input("> ")
#This line is creating a variable and assigning an open command and passing the variable file_again
#The program keeps moving down and will come back and execute this in a minute
txt_again = open(file_again)
#The line is printing the txt_again variable and telling it to read. We know txt_again will open file_again which will then prompt input from the user
print(txt_again.read())
