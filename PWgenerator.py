#PW generator 3/31 bug fix

import random
import string

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

def main():
    while True:
        length = int(input("Enter the length of the password: "))
        num_special = int(input("Enter the number of special characters: "))
        num_normal = int(input("Enter the number of normal characters: "))
        num_capital = int(input("Enter the number of capital characters: "))
        num_numbers = int(input("Enter the number of numbers: "))

        total_chars = num_special + num_normal + num_capital + num_numbers

        if total_chars > length:
                print("The sum of specific characters exceeds the desired password length. Please try again.")
        else: 
            break

    password = generate_password(length, num_special, num_normal, num_capital, num_numbers)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()