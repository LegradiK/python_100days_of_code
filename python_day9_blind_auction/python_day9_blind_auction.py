#Function with output

def format_name(f_name, l_name):
  """format first name and last name with first letter being capital letter"""
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"{formated_f_name} {formated_l_name}"
  
print(format_name("leo", "legradi"))
