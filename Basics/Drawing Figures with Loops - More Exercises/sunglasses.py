from math import ceil 

def print_lense(position, length):
  
  if position == 1 or position == n:
    print((length * 2) * "*", end="")
    
  else:
    print('*', end="")
    print(((length * 2) - 2) * "/", end="")
    print('*', end="")

n = int(input())

frame_position = ceil(n / 2)

for i in range(1, n + 1):
  
  print_lense(i, n)
  
  symbol = ""
  
  if i == frame_position:
    symbol = "|"
  else:
    symbol = " "
  
  print(symbol * n, end="")
  
  print_lense(i, n)
    
  print()
  
