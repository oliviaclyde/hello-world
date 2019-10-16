# Generate a random number between 1 and 9 (including 1 and 9). 
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 

# Extras:

# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.


import random

a = random.randint(1, 9)

def guessNumber():
    numGuesses = 0

    b = 10

    while b > 0:  
        guess = int(input("Enter a guess: "))
        if guess > a:
            print("Guess is too high. Guess again.")
        elif guess < a:
            print("Guess is too low. Guess again.")
        else:
            print("You are correct.")
            numGuesses += 1
            break
        
        numGuesses += 1
        b -= 1

    print("The number of guesses: " + str(numGuesses))

guessNumber()