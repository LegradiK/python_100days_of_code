############DEBUGGING#####################

# Describe Problem: 20 doesn't include 20. range to be changed. 
def my_function():
  for i in range(1, 21):
    if i == 20:
      print("You got it")
      
my_function()

# Reproduce the Bug: range wasn't set correctly.
from random import randint

dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)

print(dice_imgs[dice_num])

# Play Computer: 1994 wasn't included in any of the if statements.
year = int(input("What's your year of birth?"))

if year > 1980 and year <= 1994:
  print("You are a millenial.")
elif year > 1994:
  print("You are a Gen Z.")

# Fix the Errors: IndentationError for print statement:input needs to be translated into 'int': f is missing from f string
age = int(input("How old are you?"))
if age > 18:
  print(f"You can drive at age {age}.")

#Print is Your Friend: too many = in line 37
pages = 0
word_per_page = 0

pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

#Use a Debugger: Indentation error

def mutate(a_list):

  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
    
  print(b_list)

mutate([1,2,3,5,8,13])