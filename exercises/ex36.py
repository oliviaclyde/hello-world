#Designing and debugging
#Designing my own game

if __name__ == '__main__':
    print("""You open your eyes. The small light filtering around you indicates you are in a dark tunnel.
    You see the opening to three separate rooms inside this tunnel.
    You hear a faint trickling and look down. Water is starting to pool around your shoes.
    You look behind you. A rock slide has seal the tunnel entrance. You must find a way out....NOW!
    What room do you decide to enter? Room 1, 2 or 3?""")
    userInput = (input(">>  "))

    # x = 0
    # while x < 10:
    #     x += 1
    if userInput == 1:
        print("""You stumble into the first room. You see a large snake. \nDo you want to stay and fight the snake or flee?""")
        userInput = (input(">>  "))
        if userInput == "stay and fight" or userInput == "fight":
            print("You grab a rock to throw at the snake but as soon as you move the snake strikes. Venom is now coursing through your body. It's too late. You're dead.")
        elif userInput == "flee":
            print("You turn to flee and trip. The snake coils and strikes. You are dead before you hit the ground.")
        else:
            print("Not a valid input. Please try again.")
    # exit()


    # while True
    #
    #     try:
    #         break
    #
    #     except:
