from words import words
import random
import string

# ------------------ FUNCTION TO GET A WORD WITHOUT ANY SPACES OR DASH--------------------

def get_valid_word(words):
    word = random.choice(words)

    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

# ---------------------THE STARTING FUNCTION-------------------

def hangman():
    lives = 6

    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    while len(word_letters) > 0 and lives > 0:
        print("\nLives left:", lives)
        print("You have used: ", ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '_' for letter in word]
        print("Current word: ", ' '.join(word_list))

        user_input = input("Guess a letter: ").upper()

        if user_input in alphabet - used_letters:
            used_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)

            else:
                lives = lives - 1
                print("Letter not in word.")

        elif user_input in used_letters:
            print("Letter is already used, try again: ")

        else:
            print("Please enter a valid letter!!")

    if lives == 0:
        print("You LOSE!!")
    else:
        print("You WIN")


# user_input = input("Guess a letter: ").upper()
hangman()