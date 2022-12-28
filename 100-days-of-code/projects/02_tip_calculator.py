#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

# Get values for vars from the user.
print("Welcome to the tip calculator.")
bill_amount = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
pax = int(input("How many people to split the bill? "))

# Calculate the amount to be paid per person, inclusive of tip.
# Math according to PE(MD)(AS) rule
bill_per_pax = (bill_amount / pax) * (1 + tip / 100)

# Round it up to 2 decimal places
round_amount = round(bill_per_pax, 2)

# Print Output
message = f"Each person should pay: ${round_amount}"
print(message)