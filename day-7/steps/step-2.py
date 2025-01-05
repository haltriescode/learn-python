import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

# STEP 2 - Replacing Blanks
# TODO 1 - Create a "placeholder" list for the chosen word.
# For each letter in the chosen word, add a "_" to the "placeholder" list.
placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"
print(placeholder)

guess = input("Guess a letter: ").lower()

# TODO 2 - Create a "display" that puts the guess letter in the correct position in the "placeholder" list.
# If the guess letter is in the chosen word, replace the "_" in the "placeholder" list with the guess letter.

display = ""
for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"

print(display)
      