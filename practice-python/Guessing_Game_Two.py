# You, the user, will have in your head a number between 0 and 100. 
# The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.
# At the end of this exchange, your program should print out how many guesses it took to get your number.



askUser = input("Please think of a number between 0 and 100. \nI will ask a series of questions. \nPlease respond with: higher, lower, or correct. \nDo you have your number? When you are ready, type 'Go'  ")

min = 0
max = 100
guess = ((min + max)/2)

numberOfLoops = 0

# While loops make me nervous, so I'm giving it 20 iterations.
b = 20

while b > 0:
    a = input("Is your number higher or lower than " + str(guess) + "?" )
    if a == 'higher':
        min = guess
        guess = int((min + max)/2)
    elif a == 'lower':
        max = guess
        guess = int((min + max)/2)
    else:
        break
    numberOfLoops += 1
    b -= 1
print("Your number is: " + str(guess))
print("The number of guesses it took: " + str(numberOfLoops))

