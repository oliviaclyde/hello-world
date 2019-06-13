mystuff = {'apple': "I AM APPLES!"}
print(mystuff['apple'])

#this goes in mystuff.py
def apple():
    print("I AM APPLES!")



import mystuff
mystuff.apple()

def apple():
    print("I AM APPLES!")

#this is jsut a variable
tangerine = "Living reflection of a dream."

import mystuff

mystuff.apple()
print(mystuff.tangerine)

mystuff['apple'] # get apple from dict
mystuff.apple() # get apple from the module
mystuff.tangerine # same thing, it's just a variable


#A class is a way to take a group of functions and data and place
#them inside a container so you can access them with the . (dot) operator

#Creating a class like the mystuff module above

#This is the instantiate operation
class MyStuff(object): #Python looks for MyStuff() and sees it is a class you've defined

    def __init__(self): #Python looks to see if you created a "magic" __init__ function and if so, it calls that function to initialize your newly created empty object
        #inside this __init__ function you get this extra variable self which is that empty object Python made for you
        #you can set variables on it just like you would for a module, dictionary or other object
        self.tangerine = "And now a thousand years between" #This initializes the object

    def apple(self):
        print("I AM CLASSY APPLES!")


#To create modules == import module
#To create a class == instantiate class == object
#You instantiatea class by calling the class like it's a function

thing = MyStuff() #above you instatniated the class and got an object
                  #now you are taking the MyStuff object and assigning it to a variable to work with
thing.apple()
print(thing.tangerine)

#Creating a "__init__" function tells Python you've created an object (class)


#Now I have 3 ways to get things from things:
#dict style
mystuff['apples']

#module style
mystuff.apples()
print(mystuff.tangerine)

#class style
thing = MyStuff()
things.apples()
print(thing.tangerine)
