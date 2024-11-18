START = 1111
END = 9999

n = int(input())

for num in range(START, END + 1):
  
  num_string = str(num)
  
  is_special = True
  
  for digit in num_string:
    int_digit = int(digit)
    
    if int_digit == 0 or n % int_digit != 0:
      is_special = False
      break
    
  if is_special:
    print(num_string, end=" ")
