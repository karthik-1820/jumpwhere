import random
import os

def load_words(filename):
    if not os.path.exists(filename):
        with open(filename, "w") as file:
            file.write("Hands\nLegs\nIndia\nCrow\nRain\nEvaporate\n")
        print(f"'{filename}' not found. A new file has been created with default words.")
    
    with open(filename, "r") as file:
        words = [line.strip().upper() for line in file if line.strip()]
    return words

def choose_word(words):
    return random.choice(words)

def play_hangman(words):
    word = choose_word(words)
    guessed = set()
    chances = 6
    print(">>> Welcome to Hangman!")
    clue = ["_"] * len(word)

    while chances > 0 and "_" in clue:
        print(" ".join(clue))
        guess = input(">>> Guess your letter: ").upper()

        if guess in guessed:
            print("You already guessed that letter! Try again.")
            continue

        guessed.add(guess)

        if guess in word:
            for i, ch in enumerate(word):
                if ch == guess:
                    clue[i] = guess
        else:
            chances -= 1
            print(f"Incorrect! You have {chances} chances left.")

    if "_" not in clue:
        print(" ".join(clue))
        print(" Congratulations! You guessed the word.")
    else:
        print(f" Out of chances! The word was: {word}")

if __name__ == "__main__":
    words = load_words("words.txt")
    while True:
        play_hangman(words)
        again = input("Play again? (y/n): ").lower()
        if again != "y":
            break
