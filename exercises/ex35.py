from sys import exit
#You are routed to the function if you chose to "open door" after bear_moved variable was True
def gold_room():
    print("This room is full of gold. How much do you take?")
    #In theory this forces your input to be a number and converts the num to an integer instead of a float?
    #This doesn't work when I input a float...
    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    #If you didn't enter a number, then program prints and exits
    else:
        dead("Man, learn to type a number.")
    #If your number is < 50, prints and exits
    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    #If your number is >50, prints and exits
    else:
        dead("You greedy bastard!")

#You are routed to this function after the first function if you chose "left"
def bear_room():
    print("There is a bear here.")
    print("The bear has a buch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    #This variable is important!
    bear_moved = False

    while True:
        choice = input("> ")
        #This prints to the console and exits the program
        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        #If the choice is "taunt bear" AND bear_moved is NOT FALSE (meaning True....)
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            #Now the varialble is changed to true
            bear_moved = True
        #If user inputs "taunt bear" again after bear_moved is already changed to True, prints to console and exits
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        #If user inputs "open door" and bear_moved is already changed to true, you are round to a new function gold_room
        elif choice == "open door" and bear_moved:
            gold_room()
        #If none of the above inputs are chosen, message prints to console
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")
    #Goes back to the start of the program
    if "flee" in choice:
        start()
    #Exits the program
    elif "head" in choice:
        dead("Well that was tasty!")
    #Takes you to back to the beginning of the function
    else:
        cthulhu_room()

#This function prints a message to the console and exits the program
def dead(why):
    print(why, "Good job!")
    exit(0)


#This function runs first
def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input("> ")
    #This routes you to a new function
    if choice == "left":
        bear_room()
    #This routes you to a new funciton
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

#This is the start of the program and take you to the start function above
start()
