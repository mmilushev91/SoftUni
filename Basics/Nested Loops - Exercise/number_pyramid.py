n = int(input())

counter = 0

is_it_bigger = False

for row in range(1, n + 1):
  
  for col in range(1, row + 1):
    
    counter += 1 
    
    if counter > n:
      is_it_bigger = True
      break
    
    print(counter, end=" ")
  
  if is_it_bigger:
    break
  
  print()
