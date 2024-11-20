from math import ceil

n = int(input())

left_dashes = 0
right_dashes = 0
middle_dashes = 2

stars = 2

first_interval = int(ceil(n / 2))

if n % 2 != 0:
  stars = 1
  middle_dashes = 1
  
for row in range(1, first_interval + 1):
  
  if row == 1:
    dashes = n - stars
    left_dashes = int(dashes / 2)
    right_dashes = int(dashes / 2)
    
    print(left_dashes * "-", end="")
    print(stars * "*", end="")
    print(right_dashes * "-", end="")
    print()
    
    continue
  
  dashes = (n - stars) - middle_dashes
  left_dashes = int(dashes / 2)
  right_dashes = int(dashes / 2)
    
  print(left_dashes * "-", end="")
  print("*", end="")
  print(middle_dashes * "-", end="")
  print("*", end="")
  print(right_dashes * "-", end="")
  
  middle_dashes += 2
  
  print()

left_dashes = 1 
right_dashes = 1 
stars = 2

middle_dashes = n - (left_dashes + right_dashes + stars)

for row in range(first_interval + 1, n):
  print(left_dashes * "-", end="")
  print("*", end="")
  print(middle_dashes * "-", end="")
  print("*", end="")
  print(right_dashes * "-", end="")
  
  middle_dashes -= 2
  left_dashes += 1 
  right_dashes += 1
  
  print()

if n >= 3:

  if n % 2 != 0:
    print(left_dashes * "-", end="")
    print("*", end="")
    print(right_dashes * "-", end="")
    
