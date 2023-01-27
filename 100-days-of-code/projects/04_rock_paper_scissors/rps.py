rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
# Prompt the user
yourchoice = int(
    input(
        "What do you choose? Type 0 for rock, 1 for paper or 2 for scissors. ")
)

# Check Sanity
if yourchoice > 2 or yourchoice < 0:
  print("Invalid Input, Enter a number between 0 and 2.")
  exit(1)

# Create a list of the ascii art above to show the user his choice.abs
choices = [rock, paper, scissors]
print("\nYou chose:")
print(choices[yourchoice])
# Allow the computer to choose a random art.
compchoice = random.randint(0,2)
print("\nComputer chose:")
print(choices[compchoice])
# Rules of the game:
# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.
#
# Find out who won
if (yourchoice == 0) and (compchoice == 2):
  print("You win.")
elif (yourchoice == 2) and (compchoice == 1):
  print("You win.")
elif (yourchoice == 1) and (compchoice == 0):
  print("You win.")
elif (yourchoice == compchoice):
  print("It's a draw.")
else:
  print("You lose.")