import random

def hangman():
    # Predefined list of 5 words as per internship scope
    words = ["python", "coding", "alpha", "intern", "script"]
    word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("Welcome to CodeAlpha Hangman!")

    while attempts > 0:
        # Display the current state of the word
        display_word = "".join([letter if letter in guessed_letters else "_" for letter in word])
        print(f"\nWord: {display_word}")
        print(f"Attempts left: {attempts}")

        if "_" not in display_word:
            print("Congratulations! You won!")
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
        elif guess in word:
            guessed_letters.append(guess)
            print("Good guess!")
        else:
            attempts -= 1
            print("Wrong guess!")

    if attempts == 0:
        print(f"\nGame Over! The word was: {word}")

if __name__ == "__main__":
    hangman()