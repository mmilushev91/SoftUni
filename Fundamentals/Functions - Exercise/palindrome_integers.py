def solve(num_list):
  
  for num in num_list:
    
    if num == num[::-1]:
      print(True)
    else:
      print(False)
  
number_list = input().split(", ")

solve(number_list)
