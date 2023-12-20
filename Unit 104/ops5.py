# Task 1 
number = int(input("Which number do you want to check?"))

if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number")

# Task 2 
age = int(input("What is your current age"))
max_age = 90
days_in_year = 365
weeks_in_year = 52
months_in_year = 12

years_left = max_age - age
days_left = years_left * days_in_year
weeks_left = years_left * weeks_in_year
months_left = years_left * months_in_year

# Fesult
print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
