#Run with ex26.py, test2.txt = argv
#Fixed all the errors

print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
#Adding height input Here
height = input()
print("How much do you weigh?", end=' ')
weight = input()
print(f"So, you're {age} old, {height} tall and {weight} heavy.")

#This section runs correctly
#Need to import sys module
from sys import argv
script, filename = argv
#Fixed spelling of filename here
txt = open(filename)
#Adding the format f
print(f"Here's your file {filename}:")
#Fixed spelling of txt
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)
#Changing txt_again_read to txt_again.read()
print(txt_again.read())



#Need to escape the apostrophe in Let's
print('Let\'s practice everything.')
print('You\'d need to know \'bout escapes with \\ that do:')
#Adding add'l print command here
print('\n newlines and \t tabs.')


poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""


#Closing " "
print("--------------")
print(poem)
#Closing quotes
print("--------------")


#Adding 6 to end of equation
five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

#Adding : (colon) to funcion
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
#Adding operation sign
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
#Adding crates
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
#Missing underscore
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))




people = 20
#Corrected spelling of cats
cats = 30
dogs = 15



if people < cats:
#Adding ( )
    print ("Too many cats! The world is doomed!")

#Correcting operation sigh
if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

#Adding colon
if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

#Corrected = to ==
if people == dogs:
    print("People are dogs.")
