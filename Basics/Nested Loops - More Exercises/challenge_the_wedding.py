men = int(input())
women = int(input())

tables = int(input())

dates = 0

break_loop = False

for man in range(1, men + 1):
  for woman in range(1, women + 1):
    dates += 1
    
    print(f"({man} <-> {woman})", end =" ")
    
    if dates == tables:
      break_loop = True
      break
  
  if break_loop:
    break
