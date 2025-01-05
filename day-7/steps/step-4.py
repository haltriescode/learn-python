import random
stages = ['''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
============
''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
============
''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
============
''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
============
''', '''
    +---+
    |   |
    O   |
   /    |
        |
        |
============
''', '''
    +---+
    |   |
    O   |
        |
        |
        |
============
''', '''
    +---+
    |   |
        |
        |
        |
        |
============
'''

]
word_list = ["aardvark", "baboon", "camel"]


chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"
print(placeholder)

# STEP 4 - Keep track of the player's guesses.
# TODO 1 - Create a variable called "lives" to keep track of the number of lives left.
# Set "lives" to equal 6.

game_over = False
lives = 6
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
            
    print(display)
    
    # TODO 2 - If the guess is not a letter in the chosen_word, Then reduce the "lives" by 1.
    # If the lives goes down to 0 then the game should stop and it should print "You lose."

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose!")
            break

    if "_" not in display:
        game_over = True
        print("You win!")
        break

  # TODO 3 - Print the ASCII art from 'stages' 
  # that corresponds to the current number of "lives" the user has remaining.

    print(stages[lives])
    




