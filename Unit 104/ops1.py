# Multi-line comment
'''
Name: My name is Alaney.
Favorite food: My favorite food is pasta.
Dream job: My dream job is to be a Affiliate Marketer or SOC analyst. 
'''

# Assigning variables with different data types
var1 = 33          # Integer
var2 = 3.33        # Float
var3 = True        # Boolean
var4 = "Angel"     # String
var5 = [1, 2, 3]   # List

# Printing the length of a string
print(len(var4))  # Outputs: 5

# Creating 'savvy' variable and replacing a word in the string
savvy = "Learning Python is Awesome!"
savvy = savvy.replace("Awesome", "great")

# Multi-variable assignment
name, age, length = "Alaney", 25, 155

# Creating a formatted string 'miniBio'
miniBio = f"Hi my name is {name}, I am {length}cm tall and {age} years old today."

# Creating a list of mixed data types
list = [6, "python", {"Alaney":25},3.14]

# Manipulating the list
list[2] = "age"
print(list)

# Getting the length of the list
print(len(list))  # Outputs: 8

# Creating a new list 'simList'
simList = [20, 5, 10, 1, 8]

# Sorting 'simList'
simList.sort()
print(simList)

# Copying 'simList' to another list
list=simList.copy()

# Adding lists together
print(list)
