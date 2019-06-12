print("""You enter a dark room with two doors.
Do you go through door #1, door #2 or door #3?""")

door = input(">  ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input(">  ")

    if bear == "1":
        print("The bear eats your face off.  Good job!")
    elif bear == "2":
        print("The bear eats your legs off.  Good job!")
    else:
        print("Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input(">  ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")
#Adding more of my own code

elif door == "3":
    print("You are standing at the edge of a sheer cliff.")
    print("What do you do?")
    print("1. You turn and run screaming back to safe ground.")
    print("2. You take a giant step off the cliff.")
    print("3. You leap into the air and fly.")

    answer = input(">  ")

    if answer == "1":
        print("You are risk adverse.")
    elif answer == "2":
        print("You are insane.")
    else:
        print("You are a dreamer.")

else:
    #print("You stumble around and fall on a knife and die.  Good job!")
    print("Invalid input. Good-bye.")
    #How do I create a way for the user to re-enter a valid number? So that it loops back into the if statement above?
