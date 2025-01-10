import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
hard_ease = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempt_point = 0

if hard_ease == "hard":
    print("You have 5 attempts remaining to guess the number.")
    attempt_point = 5
elif hard_ease == "easy":
    print("You have 10 attempts rwmaining to guess the number.")
    attempt_point = 10

computer_number = random.randint(1,100)

while attempt_point != 0:
    guess_number = int(input("Make a guess: "))

    if guess_number == computer_number:
        print("You Win!")
        break

    elif guess_number < computer_number:
        print("Guess Higher!")
        attempt_point -= 1

    elif guess_number > computer_number:
        print("Guess Lower!")
        attempt_point -= 1

print("You Lose!")