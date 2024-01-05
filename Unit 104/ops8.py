# Your task is very simple here: write a program that uses a for loop to "count mississippi" to five.
#  Having counted to five, 
# the program should print to the screen the final message "Ready or not, here I come!"
import time

#Start code below this line:


import time

# Counting from 1 to 5 with "Mississippi" in between each count
for i in range(1, 6):
    print(i, "Mississippi")
    time.sleep(1)  # Wait for 1 second after each count

# Print the final message after counting to five
print("Ready or not, here I come!")
