word_list = ["aardvark", "baboon", "camel"]

import random

# STEP 2 - Replacing Blanks
# TODO 1 - Create a "placeholder" list for the chosen word.
# For each letter in the chosen word, add a "_" to the "placeholder" list.
chosen_word = random.choice(word_list)
print(chosen_word)

guess = input("Guess a letter: ").lower()
print(guess)

# TODO 2 - Create a "display" that puts the guess letter in the correct position in the "placeholder" list.
# If the guess letter is in the chosen word, replace the "_" in the "placeholder" list with the guess letter.

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
      