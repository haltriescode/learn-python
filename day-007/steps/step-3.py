import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"
print(placeholder)

# STEP 3 - Checking if the user has guessed all letters in the chosen word.
# TODO 1 - Use a while loop to allow the user to guess again.

guess = input("Guess a letter: ").lower()
display = ""


# TODO 2 - Change the for loop to a while loop to allow the user to guess the letters in the chosen word.

for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"
print(display)

if "_" not in display:
    print("You win!")
