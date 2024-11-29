first_limit = int(input()) + 1
second_limit = int(input()) + 1
third_limit = int(input()) + 1
    
for num1 in range(1, first_limit):
  
  if num1 % 2 != 0:
    continue
  
  for num2 in range(1, second_limit):
    
    if num2 not in [2, 3, 5, 7]:
      continue
    
    for num3 in range(1, third_limit):
      
      if num3 % 2 != 0:
        continue
      
      print(f"{num1} {num2} {num3}")
