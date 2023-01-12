# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:
# You have x days, y weeks, and z months left.
# Where x, y and z are replaced with the actual calculated numbers.

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
# Convert age to integer
int_age = int(age)
# Years remaining = 90 - age
years_remaining = 90 - int_age

# Weeks remaining = years_remaining * 52
weeks_remaining = years_remaining * 52

# Months remaining = years_remaining * 12
months_remaining = years_remaining * 12

# Days remaining = years_remaining * 365
days_remaining = years_remaining * 365

# Print as f-string
message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left."
print(message)