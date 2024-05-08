#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
import os

answer = random.randint(1,100)
EASY = 10
HARD = 5

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard':  "  ).lower()
    if level == "easy":
        return EASY
    else:
        return HARD

def replay():
    replay = input("Do you want to play again?. Type 'y' or 'n': ")
    if replay == "y":
        os.system('cls')
        game()
    else:
        print("Thank you for participating!")
        
        


def check_answer(guess, answer, attempts):
    if guess > answer:
        print("Too high.")
        return attempts - 1
    elif guess < answer:
        print("Too low")
        return attempts - 1
    else:
        print(f"You got it! The answer was {answer}")
        replay()


def game():
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100")
    
    attempts = set_difficulty()

    guess = 0
   
    while guess != answer:

        print(f"You have {attempts} attempts remaining to guess the number")
        guess = int(input("Make a guess:  "))
        attempts = check_answer(guess, answer, attempts)
        if attempts == 0:
            print("Game over. You ran out of tries.")
            replay ()
            return
        

game()