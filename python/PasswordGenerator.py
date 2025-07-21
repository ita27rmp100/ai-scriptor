import string
import secrets

def generate_password(length, has_uppercase, has_numbers, has_special_chars):
    characters = string.ascii_lowercase
    if has_uppercase:
        characters += string.ascii_uppercase
    if has_numbers:
        characters += string.digits
    if has_special_chars:
        characters += string.punctuation

    while True:
        password = ''.join(secrets.choice(characters) for _ in range(length))
        if (any(c.islower() for c in password) 
            and (not has_uppercase or any(c.isupper() for c in password)) 
            and (not has_numbers or any(c.isdigit() for c in password)) 
            and (not has_special_chars or any(c in string.punctuation for c in password))):
            return password

def main():
    length = int(input("Enter password length: "))
    has_uppercase = input("Include uppercase letters? (yes/no): ").lower() == "yes"
    has_numbers = input("Include numbers? (yes/no): ").lower() == "yes"
    has_special_chars = input("Include special characters? (yes/no): ").lower() == "yes"

    password = generate_password(length, has_uppercase, has_numbers, has_special_chars)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
