#Day 12 Final project: Number guessing game
#easy = 10 attempts
#difficult = 5 attempts
#too low/too high
#win or lose
#answer to be chosen randomly

import random

from art import logo
print(logo)

answer = random.randint(1, 101)
print(answer)

print("Welcome to the Number Guessing Game!")
print("I'm guessing a number between 1 and 100.")
difficulty = input("Choose the difficulty. Type 'easy' or 'difficult': ")

#easy
if difficulty == "easy":
  guess_chance = 10
  while guess_chance > 0:
    
    print(f"You have {guess_chance} attempts remaining to guess the answer.")
    guess = int(input("Make a guess: "))

    if guess > answer:
      print("Too high. Guess again.")
    elif guess < answer:
      print("Too low. Guess again.")
    elif guess == answer:
      print(f"Correct! The answer was {answer}")
      break
      
    guess_chance -= 1

    if guess_chance == 0:
      print("You've used all the guessing chances. Game Over.")
      break

#difficul
if difficulty == "difficult":
  guess_chance = 5
  while guess_chance > 0:
    
    print(f"You have {guess_chance} attempts remaining to guess the answer.")
    guess = int(input("Make a guess: "))

    if guess > answer:
      print("Too high.")
    elif guess < answer:
      print("Too low.")
    elif guess == answer:
      print(f"Correct! The answer was {answer}")
      break
      
    guess_chance -= 1

    if guess_chance > 0:
      print("Guess again.")
    
    if guess_chance == 0:
      print("You've used all the guessing chances. Game Over.")
      break