# Objectives
# Create if statements using these logical conditionals below. Each statement should print information to the screen depending on if the condition is met.

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
# Create an if statement using a logical conditional of your choice and include elif keyword that executes when other conditions are not met.

# Create an if statement that includes both elif and else to execute when both if and elif are not met.

# Stretch Goals (Optional Objectives)
# Pursue stretch goals if you are a more advanced user or have remaining lab time.

# Create an if statement with two conditions by using and between conditions.

# Create an if statement with two conditions by using or between conditions.

# Create a nested if statement.

# Create an if statement that includes pass to avoid errors.
a = 33
b = 22

if a == b:
    print("a is equal to b")
elif a < b:
    print("a is less than b")
else:
    print("a is greater than b")
if a < b and a != 0:
    print("a is less than b and not equal to 0")


if a > b or b != 0:
    print("Either a is greater than b or b is not equal to 0")
if a > 0:
    if b > 0:
        print("Both a and b are positive")

if a == 0:
    pass  # No action if a is zero, avoids an error
else:
    print("a is not zero")
