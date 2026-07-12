import random

print ("=" * 40)
print ("   NUMBER GUESSING GAME ")
print ("=" * 40)

secret_number = random.randint(1,100)
guesses=0

while True:
    try:
        print("Guess The Number Between 1 and 100")
        user_guess = int(input("Enter Your Guess : "))
        guesses += 1

        if user_guess < secret_number:
            print("Too low! Try again.")
        elif user_guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"\n🎉 Congratulations!")
            print(f"You guessed the number {secret_number} correctly.")
            print(f"Total attempts: {guesses}")
        
            try_again = input("Try again? (y/n): ").lower()
            if try_again != "y":
                break
            else:
                secret_number = random.randint(1,100)
                guesses=0
                print("\n")
                continue
    
    except ValueError:
        print("Invalid input! Please enter a valid integer.")


    