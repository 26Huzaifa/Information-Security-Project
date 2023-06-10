import random

def hangman():
    word_list = ["python", "java", "ruby", "javascript", "html"]
    chosen_word = random.choice(word_list)
    guessed_letters = []
    attempts = 6

    while attempts > 0:
        print("\nAttempts left:", attempts)
        masked_word = ""
        for letter in chosen_word:
            if letter in guessed_letters:
                masked_word += letter
            else:
                masked_word += "_ "
        print(masked_word)

        if masked_word == chosen_word:
            print("\nCongratulations! You guessed the word correctly.")
            break

        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        elif guess in chosen_word:
            print("Correct guess!")
            guessed_letters.append(guess)
        else:
            print("Wrong guess!")
            attempts -= 1
            guessed_letters.append(guess)

    if attempts == 0:
        print("\nGame over! You ran out of attempts.")
        print("The word was:", chosen_word)

hangman()
