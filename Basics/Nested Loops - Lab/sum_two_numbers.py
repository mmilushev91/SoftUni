start = int(input())
end = int(input())
magic_number = int(input())

counter = 0
combination_found = False

for num1 in range(start, end + 1):
  for num2 in range(start, end + 1):
    counter += 1 
    
    if num1 + num2 == magic_number:
      print(f"Combination N:{counter} ({num1} + {num2} = {magic_number})")
      combination_found = True
      break
  
  if combination_found:
    break

if not combination_found:
  print(f"{counter} combinations - neither equals {magic_number}")
