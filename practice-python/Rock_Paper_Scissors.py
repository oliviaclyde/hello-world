# Make a two-player Rock-Paper-Scissors game. 
# (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock

import random 


class RockPaperScissors: 
    print("Welcome to Rock, Paper, Scissors.....SHOOT!!")
    def __init__(self):
        self.wins = 0
        self.loses = 0
        self.ties = 0
        self.options = {"rock": 0, "paper": 1, "scissors": 2}

    # Could convert inputs to ints and compare to values in self.options and return boolean
    def logic(self, playerOne, computer):
        if playerOne == computer:
            self.ties += 1
            print("It's a tie. No one wins.") 
        elif (playerOne, computer) == ("rock", "paper"):
            self.loses += 1 
            print("Paper smothers rock. You lose.") 
        elif (playerOne, computer) == ("rock", "scissors"):
            self.wins += 1
            print("Rock crushes scissors. You win!")
        elif (playerOne, computer) == ("paper", "scissors"):
            self.loses += 1
            print("Scissors cuts paper. You lose.")
        elif (playerOne, computer) == ("paper", "rock"):
            self.wins += 1
            print("Paper smothers rock. You win!")
        elif (playerOne, computer) == ("scissors", "rock"):
            self.loses += 1
            print("Rock crushes scissors. You lose.")
        elif (playerOne, computer) == ("scissors", "paper"):
            self.wins += 1
            print("Scissors cuts paper. You win!")
        else:
            print("Invalid option. Please try again.")



    def game(self): 
        play = True
        while play:
            playerOne = input(str("What is your move?  ")).lower()
            computer = random.choice(list(self.options))
        
            print(computer)
            print(playerOne)
        
            self.logic(playerOne, computer)
            
            # Need to validate response input is a valid response, no int or invalid characters, only y or n
            response = input(str("Do you want to continue? Y/N ")).lower()
            if response == "n":
                play == False
                self.score()
                break

    def score(self):
        print("You have won", self.wins, "games.")
        print("You have lost", self.loses, "games.")
        print("You have tied", self.ties, "games.")




newGame = RockPaperScissors()

newGame.game()