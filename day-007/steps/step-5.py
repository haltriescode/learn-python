import random
from hangman_words import word_list
from hangman_art import stages

# STEP 5 - Improving the User Experience
# TODO 1 - Update the word list to use the 'word_list' from hangman_words.py

lives = 6

# TODO 3 - Import the stages from hangman_art.py and print it at the start of the game.

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False

correct_letters = []

while not game_over:

    # TODO 6 - Update th code below to tell the user how many lives they have left.
    print("************************************<???>/6 LIVES LEFT************************************")
    guess = input("Guess a letter: ").lower()
    
    # TODO 4 - If the letter has already been guessed, print the letter and let the user know it's already been guessed.
    # e.g. "You've already guessed 'x'"
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
            
    print("Word to guess: " + display)
    # TODO 5 - If the letter is not in the chosen word, print out the letter and let the user know it's not in the word.
    # e.g. "You guessed 'x', that's not in the word. You lose a life."

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True

            # TODO 7 - Print the message "You lose!" if the user has no lives left.
            print("************************************You lose!************************************")
            break

    if "_" not in display:
        game_over = True
        print("************************************You win!************************************")
        break

    # TODO 2 - Update the code below to use the stages from the file 'hangman_art.py'
    print(stages[lives])
    




