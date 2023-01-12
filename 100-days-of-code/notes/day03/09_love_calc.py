# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name = name1.lower() + name2.lower()

digit1 = name.count("t") + name.count("r") + name.count("u") + name.count("e")
digit2 = name.count("l") + name.count("o") + name.count("v") + name.count("e")

love_score = digit1 * 10 + digit2

if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score > 40) and (love_score < 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")