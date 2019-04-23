#From the sys module, import argv package
from sys import argv
#assigning two arguments to arg variable
script, input_file = argv
#Now comes defining 3 functions. The code recognizes this but no action is taken yet
#function called print_all that has one argument (f)
def print_all(f):
    print(f.read()) #Which would print to the console the reading of the file
#The position is at the end of the file after it is read. New function called rewind which take argument "f" and f.seek(0) moves back to the beginning of the file
def rewind(f):
    f.seek(0) #This moves the read position back to the beginning of the file
#New function called print_a_line which has two arguments line_count and f
def print_a_line(line_count, f):
    print(line_count, f.readline(), end=' ') #This prints to the console the first line and moves the read posiiton to the end of that line
#The end=' ' at the end of the print statment gets rid of /n assumed at the end of every printed line (will remove extra spaces)
#New variable created which opens the input_file, one of our initial argvs
current_file = open(input_file)
#This is the first piece of information that is printed to the console
print("First let's print the whole file:\n") #\n = hard return, move to next line
#This action displays the file test2.txt file because this variable opens the input_file
print_all(current_file)
#Now this is printed to the console
print("Now let's rewind, kind of like a tape.")
#This is calling the rewind funciton and passing the argument as "current_fiel" which moves the read position back to beginning
rewind(current_file)
#Print statement
print("Let's print three lines.")
#New variable set to integar 1
current_line = 1
#Calling the print_a_line function and passing two agruments: current_line, which prints to the console, and
print_a_line(current_line, current_file) #We are calling the function and passing current_line, which prints the line and current_file, which reads 1 lines at a time
#Incrementing current_line and now the read position is at the end of the first line, it will print the incremented line and the read the second line in the file
#I'm going to rewrite the following using +=
#current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)
#Incrementing current_line and now read position is at end of line 2, and reads the third line in the file
#I'm going to rewrite the following using +=
#current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)
