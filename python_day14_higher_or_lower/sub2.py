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

#First, things need to be defined. Otherwise, they won't work.
#Choosing a random item from dictionaries from game_data

A = random.choice(data)
#Get only specific items from dictionary
A_name = A['name']
A_description = A['description']
A_country = A['country']
A_follower_count = A['follower_count']

#Choose a random item for B

B = random.choice(data)
B_name = B['name']
B_description = B['description']
B_country = B['country']
B_follower_count = B['follower_count']




def make_B_A():
  A = B
#Move B data to A data
  A_name = B_name
  A_description = B_description
  A_country = B_country
  print(f"Compare A: {A_name}, {A_description}, {A_country}")  

def against_B():
  B = random.choice(data)
  
  B_name = B['name']
  B_description = B['description']
  B_country = B['country']
  
  print(f"Against B: {B_name}, {B_description}, {B_country}")

def another_game():
  #make B = A
  print(logo)
  make_B_A()
  print(vs)
  #Choose a random item for B
  against_B()


answer_correct = True
game_played = 0

#Higher Lower logo
print(logo)
 
print(f"Compare A: {A_name}, {A_description}, {A_country}")

#Printing 'vs' logo
print(vs)

print(f"Against B: {B_name}, {B_description}, {B_country}")


while answer_correct == True:
  
  #Ask user to guess A or B
  user_guess = input("Who has more followers? Type 'A' or 'B': ")
 
  
  if A_follower_count > B_follower_count and user_guess == 'A':
    answer_correct == True
    game_played += 1
    print(f"You're rignt! Current score: {game_played}")
    another_game()
    
    
    
  
  elif A_follower_count < B_follower_count and user_guess == 'B':
    answer_correct == True
    game_played += 1
    print(f"You're rignt! Current score: {game_played}")
    another_game()

    
    
  #Once user makes a mistake, count how many answers she got correct. 
  else:
    print(f"Sorry, that's wrong. Final score: {game_played}")
    answer_correct == False
    break

  

  
#Ask user which one has a higher number of followers. If the answer matches, user won. 


#Then B becomes A

#repeat it until user makes a mistake. 
#Once user makes a mistake, count how many answers she got correct. 
