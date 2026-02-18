import random;
import secrets;

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', ')', '(', '+']

print("Welcome to the password generator!")

letters_required = int(input("How many letters would you like in your password? "))
symbols_required = int(input("How many symbols would you like in your password? "))
numbers_required = int(input("How many numbers would you like in your password? "))

rand_letters = random.choices(alphabets, k = letters_required)
rand_symbols = random.choices(symbols, k = symbols_required)
rand_numbers = random.choices(numbers, k = numbers_required)


password = rand_letters + rand_symbols+ rand_numbers

secrets.SystemRandom().shuffle(password)

rand_password = ''.join(password)

print(f"Your generated password is: {rand_password}")
