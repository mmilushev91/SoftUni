n = int(input()) + 1 

for num in range(1, n):
  
  str_num = str(num)
  
  sum_num = 0
  
  for digit in str_num:
    
    sum_num += int(digit)
  
  if sum_num == 5 or sum_num == 7 or sum_num == 11:
    print(f"{num} -> {True}")
  else:
    print(f"{num} -> {False}")
