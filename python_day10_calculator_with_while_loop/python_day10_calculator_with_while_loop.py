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

def calculator():

  from art import logo
  print(logo)
  
  num1 = float(input("What's the first number?: "))
  
  for keys in operations:
    print(keys)
  
  calc_continue = True
  
  while calc_continue:
  
    operation_symbol = input("Pick an operation: ")
    
    num2 = float(input("What's the next number?: "))
    
    calculation_function = operations[operation_symbol]
    answer = round(float(calculation_function(num1, num2)),2)
      
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    continue_or_not= input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ")
    if continue_or_not == 'y':
      num1 = answer
    else:
      calc_continue = False
      calculator()

calculator()
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

