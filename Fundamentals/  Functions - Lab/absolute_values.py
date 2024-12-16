def return_abs(user_input):
  abs_list = [abs(float(num)) for num in user_input.split()]
  
  return abs_list
  
numbers = input()

print(return_abs(numbers))
