import string
import secrets

def generate_password(length, use_uppercase, use_numbers, use_special_chars):
    chars = string.ascii_lowercase
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_numbers:
        chars += string.digits
    if use_special_chars:
        chars += string.punctuation

    while True:
        password = ''.join(secrets.choice(chars) for _ in range(length))
        if (any(c.islower() for c in password) 
            and (not use_uppercase or any(c.isupper() for c in password)) 
            and (not use_numbers or any(c.isdigit() for c in password)) 
            and (not use_special_chars or any(c in string.punctuation for c in password))):
            return password

def main():
    length = int(input("Enter the password length: "))
    use_uppercase = input("Use uppercase letters? (yes/no): ").lower() == "yes"
    use_numbers = input("Use numbers? (yes/no): ").lower() == "yes"
    use_special_chars = input("Use special characters? (yes/no): ").lower() == "yes"

    password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
    print("Generated password: ", password)

if __name__ == "__main__":
    main()
