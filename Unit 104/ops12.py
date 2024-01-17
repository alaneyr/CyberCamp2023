# Your challenge tonight is to write a basic adventure game using some of the  
#code provide below and using if/elif statments

yes_no = ["yes", "no"]
directions = ["left", "right", "forward", "backward"]
 
# Introduction
name = input("What is your name, adventurer?\n")
print("Greetings, " + name + ". Let us go on a quest!")
print("You find yourself on the edge of a dark forest.")
print("Can you find your way through?\n")
 
# Start of game
response = ""
while response not in yes_no:
    response = input("Would you like to step into the forest?\nyes/no\n")
    if response == "yes":
        print("You head into the forest. You hear crows cawwing in the distance.\n")
    elif response == "no":
        print("You are not ready for this quest. Goodbye, " + name + ".")
        quit()
    else: 
        print("I didn't understand that.\n")
 
# Next part of game
response = ""

# Use if else statment from here to take you on a journey and have fun with it
# Next part of the game - Harry Potter Edition
response = ""
while response not in directions:
    response = input("You find yourself at a magical crossroads near Hogwarts. Choose a direction:\nleft/right/forward/backward\n")
    
    if response == "left":
        print("You enter the Forbidden Forest. You encounter a centaur who offers you guidance. Do you follow?\n")
        response = input("yes/no\n")
        if response == "yes":
            print("The centaur leads you to a hidden clearing with magical creatures. You gain their trust.")
        elif response == "no":
            print("You decide not to follow the centaur. The forest becomes darker, and you feel uneasy.")
        else:
            print("Your hesitation confuses the centaur, but your journey continues.")
    elif response == "right":
        print("You find the Quidditch pitch. A team invites you to play as the Seeker. Do you join the game?\n")
        response = input("yes/no\n")
        if response == "yes":
            print("You soar through the air, catching the Golden Snitch. Your house wins the game!")
        elif response == "no":
            print("You choose to watch the game. It's intense, and you enjoy the magical atmosphere.")
        else:
            print("Your indecision confuses the team, but the Quidditch match continues.")
    elif response == "forward":
        print("You reach the entrance hall where the Sorting Hat awaits. It offers to sort you into a house. Do you accept?\n")
        response = input("yes/no\n")
        if response == "yes":
            print("The Sorting Hat places you in Gryffindor! Welcome to your new house.")
        elif response == "no":
            print("You decide not to be sorted. Your journey at Hogwarts remains mysterious.")
        else:
            print("The Sorting Hat senses your uncertainty, but your Hogwarts adventure continues.")
    elif response == "backward":
        print("You decide to visit Hogsmeade. The Three Broomsticks invites you for a Butterbeer.")
    else:
        print("I didn't understand that. Choose left, right, forward, or backward.\n")