n = int(input())

for pos in range(n):
  
  side = ''
  
  if pos == 0 or pos == n - 1:
    side = '+'
  
  else:
    side = '|'
  
  print(side, end=" ")
  
  for _ in range(n - 2):
    print("-", end=" ")
  
  print(side, end=" ")
  
  print()
