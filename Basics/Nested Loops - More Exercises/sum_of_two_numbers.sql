start = int(input())
end = int(input()) + 1

magic_number = int(input())

counter = 0

loop_break = False

for num1 in range(start, end):
  
  for num2 in range(start, end):
    counter += 1
    
    if (num1 + num2) == magic_number:
      loop_break = True
      
      print(f"Combination N:{counter} ({num1} + {num2} = {magic_number})")
      break
  
  if loop_break:
    break 

else:
  print(f"{counter} combinations - neither equals {magic_number}")
