import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

print("=" * 40)
print("     ROCK PAPER SCISSORS")
print("=" * 40)

while True:

    print("\nChoose one:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("0. Exit")

    try:
        choice = int(input("\nEnter your choice: "))

        if choice == 0:
            print("\nThanks for playing!")
            print(f"Final Score -> You: {user_score} | Computer: {computer_score}")
            break

        if choice not in [1, 2, 3]:
            print("Invalid choice. Please select 1, 2, or 3.")
            continue

        user_choice = choices[choice - 1]
        computer_choice = random.choice(choices)

        print(f"\nYou chose      : {user_choice.capitalize()}")
        print(f"Computer chose : {computer_choice.capitalize()}")

        if user_choice == computer_choice:
            print("\n🤝 It's a Draw!")

        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
        ):
            print("\n🎉 You Win!")
            user_score += 1

        else:
            print("\n💻 Computer Wins!")
            computer_score += 1

        print(f"\nScore")
        print(f"You      : {user_score}")
        print(f"Computer : {computer_score}")

    except ValueError:
        print("Please enter a valid number.")