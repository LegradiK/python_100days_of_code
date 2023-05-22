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

user_choise = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors: "))
if user_choise == 0:
  print(rock)
elif user_choise == 1:
  print(paper)
elif user_choise == 2:
  print(scissors)

comp_choise = random.randint(0, 2)
if comp_choise == 0:
  print(rock)
elif comp_choise == 1:
  print(paper)
elif comp_choise == 2:
  print(scissors)

if (user_choise == 0 and comp_choise == 2) or (user_choise == 1 and comp_choise == 0) or (user_choise == 2 and comp_choise == 1):
  print("You won!")
elif (user_choise == 0 and comp_choise == 1) or (user_choise == 1 and comp_choise == 2) or (user_choise == 2 and comp_choise == 0):
  print("You lost!")
elif (user_choise == 0 and comp_choise == 0) or (user_choise == 1 and comp_choise == 1) or (user_choise == 2 and comp_choise == 2):
  print("Draw")
