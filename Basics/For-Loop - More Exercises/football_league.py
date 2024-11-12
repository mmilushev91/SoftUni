stadium_capacity = int(input())
fans_count = int(input())

sector_a, sector_b, sector_v, sector_g = 0, 0, 0,0

for _ in range(fans_count):
  sector = input()
  
  if sector == "A":
    sector_a += 1 
  
  elif sector == "B":
    sector_b += 1 
  
  elif sector == "V":
    sector_v += 1 
  
  elif sector == "G":
    sector_g += 1 

print(f"{sector_a / fans_count * 100:.2f}%")
print(f"{sector_b / fans_count * 100:.2f}%")
print(f"{sector_v / fans_count * 100:.2f}%")
print(f"{sector_g / fans_count * 100:.2f}%")
print(f"{fans_count / stadium_capacity * 100:.2f}%")
