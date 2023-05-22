from art import logo
print(logo)

#Calculator functions

#adding
def add(num1, num2):
  """add n1 + n2"""
  return num1 + num2
#substract
def substract(num1, num2):
  """substract n1 - n2"""
  return num1 - num2
#multiply
def multiply(num1, num2):
  """multiply n1 * n2"""
  return num1 * num2
#divide
def divide(num1, num2):
  """divide n1 / n2"""
  return num1 / num2

operations = {
  "+" : add,
  "-" : substract,
  "*" : multiply,
  "/" : divide
}

num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))

for keys in operations:
  print(keys)

operation_symbol = input("Pick an operation from the line above: ")

calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)


print(f"{num1} {operation_symbol} {num2} = {answer}")


# #make lists out of dictionary keys and values
# keys_list = list(operations.keys())
# values_list = list(operations.values())
# #find where operation_symbol is in keys_list
# operation_position = keys_list.index(operation_symbol)
# #find where operation_symbol is
# operation_symbol = values_list[operation_position]



# if operation_symbol == "add":
#   answer = add(num1, num2)
# elif operation_symbol == "substract":
#   answer = substract(num1, num2)
# elif operation_symbol == "multiply":
#   answer = int(multiply(num1, num2))
# elif operation_symbol == "divide":
#   answer = int(divide(num1, num2))

# operation_symbol = keys_list[operation_position]

