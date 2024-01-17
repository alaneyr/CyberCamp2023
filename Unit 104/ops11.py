import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []

# Generate random letters
for char in range(1, nr_letters + 1):
    password.append(random.choice(letters))

# Generate random symbols
for char in range(1, nr_symbols + 1):
    password.append(random.choice(symbols))

# Generate random numbers
for char in range(1, nr_numbers + 1):
    password.append(random.choice(numbers))

# Randomize the order of characters in the password
random.shuffle(password)

# Convert the password list to a string
password_str = ''.join(password)

# Print the generated password
print(f"Your randomized password is: {password_str}")