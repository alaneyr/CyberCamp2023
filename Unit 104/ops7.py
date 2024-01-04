# Bob wants to create a guessing number game! 
# Rule 1: Numbers have to be between 1 and 20
# Rule 2: Program must run until the correct number is guessed
# Rule 3: When guessed right, print out how many tries to guess the 
# right number. Example: "Yes! You guessed it in ___ guesses."
# Rule 4: The program will tell you if your number needs to be HIGHER
# or LOWER 
# until the number is guessed correctly and the program ENDS.
# Remeber to import the random function
#Bonus objective can you put it into a loop to make the game end after 3 turns?

import random

secret_number = random.randint(1, 20)
attempts = 0

while True:
    guess = int(input("Guess the number between 1 and 20: "))
    attempts += 1

    if guess == secret_number:
        print(f"Yes! You guessed it in {attempts} {'attempt' if attempts == 1 else 'attempts'}.")
        break
    elif guess < secret_number:
        print("Try again. The number is higher.")
    else:
        print("Try again. The number is lower.")
