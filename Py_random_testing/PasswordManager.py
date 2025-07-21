import getpass
import hashlib
import secrets
import string
import os

class PasswordManager:
    def __init__(self, master_password):
        self.master_password = self.hash_password(master_password)
        self.passwords = self.load_passwords()

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def load_passwords(self):
        if os.path.exists('passwords.txt'):
            with open('passwords.txt', 'r') as f:
                return [line.strip().split(',') for line in f.readlines()]
        else:
            return []

    def save_passwords(self):
        with open('passwords.txt', 'w') as f:
            for password in self.passwords:
                f.write(','.join(password) + '\n')

    def generate_password(self, length):
        return ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))

    def add_password(self, platform, password):
        self.passwords.append([platform, password])
        self.save_passwords()

    def get_password(self, platform):
        for p in self.passwords:
            if p[0] == platform:
                return p[1]
        return None

    def update_password(self, platform, new_password):
        for i, p in enumerate(self.passwords):
            if p[0] == platform:
                self.passwords[i][1] = new_password
                self.save_passwords()
                break

    def delete_password(self, platform):
        self.passwords = [p for p in self.passwords if p[0] != platform]
        self.save_passwords()

def main():
    master_password = getpass.getpass('Enter master password: ')
    pm = PasswordManager(master_password)

    while True:
        print('1. Add password')
        print('2. Get password')
        print('3. Update password')
        print('4. Delete password')
        print('5. Generate password')
        print('6. Quit')

        choice = input('Choose an option: ')

        if choice == '1':
            platform = input('Enter platform: ')
            password = getpass.getpass('Enter password: ')
            pm.add_password(platform, password)
        elif choice == '2':
            platform = input('Enter platform: ')
            password = pm.get_password(platform)
            if password:
                print(password)
            else:
                print('No password found for this platform')
        elif choice == '3':
            platform = input('Enter platform: ')
            new_password = getpass.getpass('Enter new password: ')
            pm.update_password(platform, new_password)
        elif choice == '4':
            platform = input('Enter platform: ')
            pm.delete_password(platform)
        elif choice == '5':
            length = int(input('Enter password length: '))
            print(pm.generate_password(length))
        elif choice == '6':
            break
        else:
            print('Invalid option')

if __name__ == '__main__':
    main()
