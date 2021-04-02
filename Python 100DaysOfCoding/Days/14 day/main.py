from replit import clear
import random as r
from art import logo,vs
from game_data import data

def get_random_account():
    return r.choice(data)

def format_data_description(data):
    name = data["name"]
    description = data["description"]
    country = data["country"]

    return f"{name}, a {description}, from {country}."

def check_answer(guess, account_a, account_b):
    if account_a > account_b:
        return guess == 'a'
    else:
        return guess == 'b'

def game():
    print(logo)
    score = 0
    account_a = get_random_account()
    account_b = get_random_account()
    game_should_continue = True

    while game_should_continue:
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data_description(account_a)}")
        print(vs)
        print(f"Against B: {format_data_description(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_followers = account_a["follower_count"]
        b_followers = account_b["follower_count"]
        is_right = check_answer(guess, a_followers, b_followers)

        clear()
        print(logo)
        if is_right:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

game()