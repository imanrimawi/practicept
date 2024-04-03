import random
import string

def introduction():
    print("Hello! Welcome to the password generator! Please answer the following questions, so the program can create you a password")

def generate_password(length, use_digits=True, use_punctuation=True):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def get_user_choice():
    use_digits = input("Would you like the password to include digits? (yes/no): ").lower().startswith('y')
    use_punctuation = input("Would you like the password to include punctuation? (yes/no): ").lower().startswith('y')
    return use_digits, use_punctuation

introduction()

while True:
    length = int(input("Please enter your desired length of the password: "))
    use_digits, use_punctuation = get_user_choice()

    password = generate_password(length, use_digits, use_punctuation)
    print("Here is your generated Password:", password)

    regenerate = input("Would you like to generate a new password? (yes/no): ").lower()
    if regenerate == 'no':
        print("Thank you for using my password generator!!")
        break



