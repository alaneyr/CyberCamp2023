# Scenario
# A junior magician has picked a secret number. He has hidden it in a variable named secret_number.
#  He wants everyone who runs his program to play the Guess the secret number game, 
#  and guess what number he has picked for them. 
#  Those who don't guess the number will be stuck in an endless loop forever! Unfortunately, he does not know how to complete the code.

# Your task is to help the magician complete the code in the editor in such a way so that the code:
# will ask the user to enter an integer number;
# will use a while loop;
# will check whether the number entered by the user is the same as the number picked by the magician. 
# If the number chosen by the user is different than the magician's secret number, the user should see 
# the message "Ha ha! You're stuck in my loop!" and be prompted to enter a number again. 
# If the number entered by the user matches the number picked by the magician, the number should be printed to the screen, 
# and the magician should say the following words: "Well done, muggle! You are free now."
# The magician is counting on you! Don't disappoint him.

# The magician's secret number
secret_number = 333  # You can change this number to any integer of your choice

# Asking the user to guess the secret number using a while loop
while True:
    user_number = int(input("Enter an integer number: "))  # Asking user for input
    
    if user_number == secret_number:  # Checking if the user's number matches the secret number
        print(f"Well done, muggle! You are free now. The secret number was {secret_number}.")
        break  # Exiting the loop if the numbers match
    else:
        print("Ha ha! You're stuck in my loop!")  # Prompting user to try again if the numbers don't match