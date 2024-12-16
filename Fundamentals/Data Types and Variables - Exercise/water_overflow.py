MAX_LIMIT = 255

tank_level = 0

n = int(input())

for _ in range(n):
  litters = int(input())
  
  if litters + tank_level > MAX_LIMIT:
    print("Insufficient capacity!")
    continue
  
  tank_level += litters

print(tank_level)
