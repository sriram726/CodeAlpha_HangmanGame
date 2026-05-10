# TASK: Hangman Game

import random

# List of predefined words
words = ["apple", "tiger", "chair", "pizza", "robot"]

# Randomly choose a word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of wrong guesses allowed
wrong_guesses = 6

print("=================================")
print("         HANGMAN GAME")
print("=================================")

# Game loop
while wrong_guesses > 0:

    # Display word with blanks
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if word is guessed
    if "_" not in display_word:
        print("\nCongratulations! You guessed the word.")
        break

    # User input
    guess = input("Enter a letter: ").lower()

    # Check letter
    if guess in word:
        print("Correct Guess!")
        guessed_letters.append(guess)

    else:
        wrong_guesses -= 1
        print("Wrong Guess!")
        print("Remaining chances:", wrong_guesses)

# If player loses
if wrong_guesses == 0:
    print("\nGame Over!")
    print("The word was:", word)