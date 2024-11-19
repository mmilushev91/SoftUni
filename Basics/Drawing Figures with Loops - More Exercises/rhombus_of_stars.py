n = int(input())

for i in range(1, n + 1):
  white_spaces = n - i
  print(white_spaces * " ", end="")
  print(i * "* ", end="")
  print()

for i in range(1, n + 1):
  stars = n - i
  
  print(i * " ", end="")
  print(stars * "* ", end="")
  print()
  
