#PW generator 3/31 bug fix

import random
import string
import json
import os

def generate_password(length, num_special, num_normal, num_capital, num_numbers):
    special_chars = string.punctuation
    normal_chars = string.ascii_lowercase
    capital_chars = string.ascii_uppercase
    numbers = string.digits

    password_list = []

    # Add special characters
    for _ in range(num_special):
        password_list.append(random.choice(special_chars))

    # Add normal characters
    for _ in range(num_normal):
        password_list.append(random.choice(normal_chars))

    # Add capital characters
    for _ in range(num_capital):
        password_list.append(random.choice(capital_chars))

    # Add numbers
    for _ in range(num_numbers):
        password_list.append(random.choice(numbers))

    # Fill the remaining length with random characters
    remaining_length = length - (num_special + num_normal + num_capital + num_numbers)
    for _ in range(remaining_length):
        password_list.append(random.choice(string.ascii_letters + string.digits + string.punctuation))

    # Shuffle the password list
    random.shuffle(password_list)

    # Join the characters to form the password
    password = ''.join(password_list)

    return password

def save_password(password, purpose, filename="passwords.json"):
    try:
        with open(filename, 'r') as file:
            # Read the existing data
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    except json.JSONDecodeError:
        data = {}

    # Update the file with the new password
    with open(filename, 'w') as file:
        data[purpose] = password
        json.dump(data, file, indent=4)

def retrieve_password(purpose, filename="passwords.json"):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data.get(purpose, "Password not found for this purpose.")
    except (FileNotFoundError, json.JSONDecodeError):
        return None

def print_saved_passwords(filename="passwords.json"):
    if not os.path.isfile(filename):
        print("No passwords have been saved yet. Please generate a password first.")
        return False
    with open(filename, 'r') as file:
        data = json.load(file)
        if data:
            print("Saved passwords for the following:")
            for purpose in data:
                print(f"- {purpose}")
            return True
        else:
            print("No passwords have been saved yet. Please generate a password first.")
            return False

def main_menu():
    while True:
        print("\nPassword Manager:")
        print("1. Generate a new password")
        print("2. Retrieve a saved password")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            main()
        elif choice == "2":
            if print_saved_passwords():
                purpose = input("Enter the : ")
                password = retrieve_password(purpose)
                if password:
                    print(f"Password for {purpose}: {password}")
                else:
                    print("No password found for this application. Please generate a password.")
        elif choice == "3":
            print("Exiting the Password Manager.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def main():
    length = int(input("Enter the length of the password: "))
    num_special = int(input("Enter the number of special characters: "))
    num_normal = int(input("Enter the number of normal characters: "))
    num_capital = int(input("Enter the number of capital characters: "))
    num_numbers = int(input("Enter the number of numbers: "))

    password = generate_password(length, num_special, num_normal, num_capital, num_numbers)
    print("Generated Password:", password)

    purpose = input("Please enter what this password will be used for: ")
    save_password(password, purpose)
    print(f"Your new password for {purpose} has been saved successfully.")

if __name__ == "__main__":
    main_menu()