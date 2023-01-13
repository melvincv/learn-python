# You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
# Line 17 splits the string names_string into individual names and puts them inside a List called names. For this to work, you must enter all the names as names followed by comma then space. e.g. name, name, name

# Example Input
# Angela, Ben, Jenny, Michael, Chloe
# Note: notice that there is a space between the comma and the next name.

# Example Output
# Michael is going to buy the meal today!
# Hint
# You might need the help of the len() function.

# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Find the number of elements in the list - 1
# As List index starts from 0
name_count = len(names) - 1

# Select a random integer between 0 and name_count
rand_int = random.randint(0,name_count)
print(f"{names[rand_int]} is going to buy the meal today!")