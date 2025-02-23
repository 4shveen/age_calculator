'''Age Calculator with Birthday Countdown
Objective:
Create a Python program that calculates a person's age based on their birth year and
determines the number of days remaining until their next birthday. The program should
automatically fetch the current date and time from the system.
Key Concepts:
● Variables & arithmetic expressions
● Working with dates & time (datetime module)
● Conditional logic
Task:
● Prompt the user to enter their birth year, month, and day.
● Compute their current age.
● Determine the date of their next birthday.
● Calculate and display the countdown (in days) to their upcoming birthday.'''

# Prompt the user for input
year = int (input("Enter your birth year: "))
month = int (input("Enter your birth month: "))
day = int (input("Enter your birth day: "))

# Get current date and time
from datetime import date
today = date.today()

print(f"Today's date is: {today}")
print(f"You were born on: {year}/{month}/{day}")

# Calculate age
age = today.year - year
if (today.month, today.day) < (month, day) :
    age -= 1

# Determine next birthday
next_birthday = date (today.year, month, day)
if (next_birthday) <= today :
    next_birthday = date (today.year + 1, month, day)

# Calculate number of days until next birthday
countdown = (next_birthday - today).days

# Display results
print(f"You are {age} years old.")
print(f"Your next birthday is on {next_birthday}.")
print(f"Countdown to your next birthday: {countdown} days.")