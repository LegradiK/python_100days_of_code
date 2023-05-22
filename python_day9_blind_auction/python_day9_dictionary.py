programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
  "Loop": "Action of doing something over and over again.",
}

# #Retrieving data from dictionary

# print(programming_dictionary["Loop"])

# #Adding

# programming_dictionary["Print"] = "Print anything asked when run the programming"
# print(programming_dictionary)

# #Delete everything in the dictionary
# programming_dictionary = {}

# print(programming_dictionary)

#Loop through dictionary

for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])