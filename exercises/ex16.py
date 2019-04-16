from sys import argv #We import the sys module and the argv package

script, filename = argv #We have defined two variables for the argv

print(f"We're going to erase {filename}.") #Print statement that references a format string filename
print("If you don't want that, hit CTRL-C (^C).") #Print statement
print("If you do want that, hit RETURN.") #Print statement

input("?") #Prints a question mark but the program is also waiting for user input

print("Opening the file...") #Print statement
target = open(filename, 'w') #new variable called target with the open function. This opens our filename in "write" mode with overwrites everything in the file

print("Truncating the file. Goodbye!") #Print statment
target.truncate() #Truncate function () without set parameters will overwite entire file. This is redundant since we opened the file in write mode

print("Now I'm going to ask you for three lines.") #Print statement

line1 = input("Line 1: ") #New variable defined with user input
line2 = input("Line 2: ") #New variable defined with user input
line3 = input("Line 3: ") #New variable definted with user input

print("I'm going to write these to the file.") #Print statement
target.write(f"{line1}\n{line2}\n{line3}\n".format(line1, line2, line3)) #Calling the write command on the target variable for three lines of text using formats, strings and escape characters
#Trying another way
#target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")
#And another....
#target.writelines([line1, line2, line3]) #This puts the text all on one line

"""
#Original exercise wrote each line
target.write(line1) #Calling the target variable (which opens our filename in write mode) with a write function and passing our 1st variable
target.write("\n") #Hard returns to new line
target.write(line2) #Calling the target variable again and passing our 2nd variable
target.write("\n") #Hard return to new line
target.write(line3) #Calling the target variable and passing our 3rd variable
target.write("\n") #Hard return to new line
"""
print("And finally, we close it.") #Print statement
target.close() #Calling target variable with close function to close the file

#Adding script to open and read the file I just created
print(f"Here's your file {filename}: ") #Print statement
target = open(filename, 'r') #I have to define target again because I closed the file. If I don't do this (or something similiar) I can't call a read function on a closed variable
print(target.read()) #I am calling the read function on the target variable
print = ("Goodbye") #Print statement
target.close() #Close file
