from math import ceil

n = int(input())

stars_count = 1 
row = 0

if n % 2 == 0:
  stars_count = 2

while True:
  side_dashes = ceil((n - stars_count) / 2)
  row += 1
  
  print(side_dashes * "-", end="")
  print(stars_count * "*", end="")
  print(side_dashes * "-", end="")
  print()
    
  stars_count += 2
    
  if stars_count == n:
    
    print(stars_count * "*")
      
    break
  
  elif stars_count > n:
    break

stars_count = n - 2
interval = n - row

for i in range(1, interval):
  print("|", end="")
  print(stars_count * "*", end="")
  print("|", end="")
  print()
  
