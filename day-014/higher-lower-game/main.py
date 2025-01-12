from data import data
from art import logo, vs
import random


game_should_continue = True
score = 0
print(logo)

def format_data(account):
        '''Format the account data into printable format'''
        account_name = account["name"]
        account_desc = account["description"]
        account_country = account["country"]
        return f"{account_name}, a {account_desc}, from {account_country}"
    
    

def check_ans(user_guess, a_follower, b_follower):
    if a_follower > b_follower:
        return user_guess == "a" or user_guess == "A"
    else:
        return user_guess == "b" or user_guess == "B"

while game_should_continue:
    a = random.choice(data)
    b = random.choice(data)

    while a == b:
        b = random.choice(data)

    print(f"Compare A: {format_data(a)}.")
    print(vs)
    print(f"Compare B: {format_data(b)}.")
    guess = input("Guess who has more followers, Type 'A' or 'B': ")

    a_follower = a.get("follower_count")
    b_follower = b.get("follower_count")
    
        
    is_correct = check_ans(guess, a_follower, b_follower )
    if is_correct:
        score += 1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue = False


