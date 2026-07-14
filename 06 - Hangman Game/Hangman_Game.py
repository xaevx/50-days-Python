import random

words = [
    "python",
    "developer",
    "computer",
    "keyboard",
    "programming",
    "hangman",
    "algorithm",
    "internet",
    "software",
    "database"
]

secret_word = random.choice(words)
guessed_letters = []
attempts = 6

print("=" * 40)
print("         HANGMAN GAME")
print("=" * 40)

while attempts > 0:

    display = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print(f"\nWord : {display}")
    print(f"Attempts Left : {attempts}")

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Correct!")
    else:
        attempts -= 1
        print("❌ Wrong Guess!")

    if all(letter in guessed_letters for letter in secret_word):
        print(f"\nCongrats! You guessed the word '{secret_word}'.")
        break

else:
    print("\n💀 Game Over!")
    print(f"The correct word was: {secret_word}")