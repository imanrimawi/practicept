import random
import string

def generate_password(length, use_digits=True, use_punctuation=True, difficult=True):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation

    if not difficult:
        characters = string.ascii_letters + string.digits

    return ''.join(random.choice(characters) for _ in range(length))

def get_user_choice():
    use_digits = input("Include digits? (yes/no): ").lower().startswith('y')
    use_punctuation = input("Include punctuation? (yes/no): ").lower().startswith('y')
    difficult = input("Make it more difficult? (yes/no): ").lower().startswith('y')
    return use_digits, use_punctuation, difficult

while True:
    length = int(input("Enter the length of the password: "))
    use_digits, use_punctuation, difficult = get_user_choice()

    password = generate_password(length, use_digits, use_punctuation, difficult)
    print("Generated Password:", password)

    regenerate = input("Generate another password? (yes/no): ").lower()
    if regenerate.startswith('n'):
        break



