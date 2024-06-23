import string
import random

def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    
    if not characters:
        raise ValueError("No character sets selected for password generation.")

    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    
    length = int(input("Enter the desired length of the password: "))

    
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    use_special = input("Include special characters? (yes/no): ").lower() == 'yes'

    
    try:
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
        
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
