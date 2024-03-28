import random

def choose_word():
    words = ["apple", "banana", "orange", "grape", "kiwi", "strawberry", "blueberry", "peach", "watermelon", "pineapple"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("The word contains", len(word), "letters.")

    while True:
        print("\nWord:", display_word(word, guessed_letters))
        print("Attempts left:", attempts)
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        elif guess in word:
            guessed_letters.append(guess)
            if set(guessed_letters) == set(word):
                print("\nCongratulations! You've guessed the word:", word)
                break
        else:
            print("Incorrect guess.")
            attempts -= 1
            if attempts == 0:
                print("\nSorry, you've run out of attempts. The word was:", word)
                break

hangman()
