import art
import random as r


EASY_LEVEL = 10
HARD_LEVEL = 5

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def check_guess(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You've got it! The answer is {answer}")

def game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    turns = set_difficulty()
    answer = r.randint(1, 100)
    print(f"Psst. The answer is {answer}.")

    guess = 0
    while guess != answer:

        print(f"You have {turns} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))

        turns = check_guess(guess, answer, turns)

        if turns == 0:
            print("You've run out of guesses, you lose!")
            return
        elif guess != answer:
            print("Guess again.")

game()