import random
import string 

def generate_password(use_upper, use_lower, use_digits, use_symbols, length):
    characters = ""

    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase 
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return None

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password

while True:  
    print("\n" + "=" * 40)
    print("       PASSWORD GENERATOR")
    print("=" * 40)

    try:

        length = int(input("Password Length : "))

        upper = input("Include Uppercase? (y/n): ").lower() == "y"
        lower = input("Include Lowercase? (y/n): ").lower() == "y"
        digits = input("Include Numbers? (y/n): ").lower() == "y"
        symbols = input("Include Symbols? (y/n): ").lower() == "y"

        password = generate_password(
            use_upper=upper,
            use_lower=lower,
            use_digits=digits,
            use_symbols=symbols,
            length=length
        )

        if password:
            print("\nGenerated Password")
            print("-" * 20)
            print(password)
        else:
            print("\nPlease select at least one character type.")

        again = input("\nGenerate Another? (y/n): ").lower()

        if again != "y":
            print("\nGoodbye!")
            break

    except ValueError:
        print("\nInvalid input! Please enter a valid integer for the password length.")

    except Exception as error:
        print(f"\nUnexpected Error: {error}")