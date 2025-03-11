"""
Classwork (c)Masterschool

Create a "Guessing Game"!

For each game, select a random number from 1 to 9(inclusive).
The player has [three attempts] to guess the number.
Inform the player if they win or lose.

[Extra]
After each guess, "throw a dice" by selecting a number from 1 to 6(inclusive).
If the "dice" shows 5 or 6, the player gets another attempt to guess the number.
Inform the player of the dice results.

(c)2025 Justus Decker - My solution
"""

from random import randint

class GuessingGame:
    def __init__(self) -> None: 
        self.random_num_max = 9
    def run(self) -> None:
        guess_number = randint(1,self.random_num_max)
        guesses_left = 3
        guesses = []
        while guess_number != 0:
            player_input:str = ''
            while player_input == '' or not player_input.isdecimal() or player_input in guesses or len(player_input) > 1:
                player_input = input(f"Guess a number between [1 to {self.random_num_max}]: ")
                #Inform the player about the wrong input
                if player_input == '': print("Input cant be empty!")
                elif not player_input.isdecimal(): print("Input must be an integer!")
                if player_input in guesses: print("You have already guessed this number!")
                if len(player_input) > 1: print("The number is too long!")
            
            guesses.append(player_input)    #Add the player guess to the list so it cant be guesses again!
            
            if guess_number == int(player_input):
                print(f"You won! The number was [{guess_number}]")
                return
            
            #check for remaining guesses
            if not guesses_left:
                print(f"You lose! The number was [{guess_number}]")
                return
            else:
                print(f"Wrong guess. [{guesses_left}] guesses left")
                
            #throw a dice if the number is 5 or 6, the player get a free guess
            if randint(1,6) not in [5,6]:
                print(f"You got a free guess. [{guesses_left}] guesses left")
                guesses_left -= 1
            else:
                print(f"Unlucky... no guess for you.")
GG = GuessingGame()
GG.run()