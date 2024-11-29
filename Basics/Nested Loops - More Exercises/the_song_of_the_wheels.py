m = int(input())

pair_counter = 0
password = None

for a in range(1, 10):
  for b in range(1, 10):
    
    if a >= b:
      continue
    
    for c in range(1, 10):
      
      for d in range(1, 10):
        if c <= d:
          continue
        
        if (a*b + c*d ) != m:
          continue
        
        pair_counter += 1
        
        print(f"{a}{b}{c}{d}", end=" ")
        
        if pair_counter == 4:
          password = f"{a}{b}{c}{d}"

print()
if password:
  print(f"Password: {password}")
else:
  print("No!")
