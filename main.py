import random
import string

def generate_password(length, include_uppercase, include_numbers, include_symbols):
    # Base character set (lowercase letters)
    characters = string.ascii_lowercase

    # Add optional character sets
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    # Validate password length
    if length < 4:
        raise ValueError("Password length must be at least 4 characters for a secure password.")

    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))

    # Enforce at least one character of each selected type
    password = ensure_inclusion(password, include_uppercase, include_numbers, include_symbols)

    return password

def ensure_inclusion(password, include_uppercase, include_numbers, include_symbols):
    """
    Ensure the generated password includes at least one character
    from each selected category (if applicable).
    """
    password_list = list(password)
    if include_uppercase:
        replace_random(password_list, string.ascii_uppercase)
    if include_numbers:
        replace_random(password_list, string.digits)
    if include_symbols:
        replace_random(password_list, string.punctuation)
    random.shuffle(password_list)  # Shuffle to randomize placement
    return ''.join(password_list)

def replace_random(password_list, character_set):
    """
    Replace a random character in the password with one from the specified set.
    """
    index = random.randint(0, len(password_list) - 1)
    password_list[index] = random.choice(character_set)

def get_user_input():
    """
    Collect and validate user input for password generation preferences.
    """
    print("Welcome to the Password Generator!")
    print("Follow the instructions to customize your secure password.\n")

    while True:
        try:
            length = int(input("Enter the desired password length (minimum 4): "))
            if length < 4:
                raise ValueError
            break
        except ValueError:
            print("Invalid input! Please enter an integer value of at least 4.")

    include_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

    return length, include_uppercase, include_numbers, include_symbols

if __name__ == "__main__":
    # Get user input
    length, include_uppercase, include_numbers, include_symbols = get_user_input()

    try:
        # Generate password
        password = generate_password(length, include_uppercase, include_numbers, include_symbols)
        print("\nYour Secure Password:")
        print(f"{password}")
    except ValueError as e:
        print(f"Error: {e}"
