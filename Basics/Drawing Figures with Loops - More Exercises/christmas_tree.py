n = int(input())

print(n * ' ', end="")
print(" | ")

for i in range(1, n + 1):
  white_spaces = n - i
  
  print(white_spaces * ' ', end="")
  print(i * "*", end="")
  
  print(" | ", end="")
  
  print(i * "*", end="")
  
  print()
  
