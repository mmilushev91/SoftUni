electrons = int(input())

shell = []
n = 0

while electrons > 0:
  n += 1 
  
  electrons_to_add = 2 * n ** 2
  
  if electrons_to_add > electrons:
    electrons_to_add = electrons
  
  electrons -= electrons_to_add
  shell.append(electrons_to_add)
    
print(shell)
