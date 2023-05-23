#Compare A
#Against B
#Who has more followers? Type 'A' or 'B': 

#Previous B becomes A

#Game over once you make a mistake
#It will show your score

#Data is saved in dictionaries

#Importing all the important elements
from art import logo
from art import vs
from game_data import data
import random

#to clear the inputs
import os

#Randomly choosing A
A = random.choice(data)

#Getting data from game_data.py
A_name = A['name']
A_follower_count = A['follower_count']
A_description = A['description']
A_country = A['country']

print(f"{A_name}, {A_follower_count}, {A_description}, {A_country}")


#Randomly choosing B
B = random.choice(data)

#Getting data from game_data.py
B_name = B['name']
B_follower_count = B['follower_count']
B_description = B['description']
B_country = B['country']

print(f"{B_name}, {B_follower_count}, {B_description}, {B_country}")


#what to be displayed for comparing
print(logo)

print(f"Compare A: {A_name}, {A_description}, {A_country}, {A_follower_count}")

print(vs)

print(f"Against B: {B_name}, {B_description}, {B_country}, {B_follower_count}")

def move_B_to_A():
  B = A
  B_name = A_name
  B_description = A_description
  B_country = A_description
  B_follower_count = A_follower_count
  print(f"Compare A: {A_name}, {A_description}, {A_country}, {A_follower_count}")

def random_B():
  #Randomly choosing B
  B = random.choice(data)

  #Getting data from game_data.py
  B_name = B['name']
  B_follower_count = B['follower_count']
  B_description = B['description']
  B_country = B['country']

  print(f"{B_name}, {B_follower_count}, {B_description}, {B_country}")


#Ask user which has higher num of followers. A or B
user_input = input("Who has more followers? Type A or B: ")

number_played = 0

play_again = True

def compare_follower_count():
  if A_follower_count > B_follower_count and user_input == "A":
      number_played += 1
      print(f"You're right! Current score: {number_played} ")
  elif A_follower_count < B_follower_count and user_input == "B":
      number_played += 1
      print(f"You're right! Current score: {number_played} ")
  else:
      print(f"Sorry, that's wrong. Final score: {number_played}")


while play_again == True:
  
