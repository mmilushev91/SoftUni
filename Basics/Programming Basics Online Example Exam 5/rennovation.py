from math import ceil

height = int(input())
width = int(input())

total_surface = (height * width) * 4

not_to_be_painted = (int(input()) / 100) * total_surface

to_be_painted_sq_m = ceil(total_surface - not_to_be_painted)

command = input()

total_paint = 0

while command != "Tired!":
  paint = int(command)
  
  total_paint += paint
  
  if total_paint > to_be_painted_sq_m:
    paint_left = total_paint - to_be_painted_sq_m
    print(f"All walls are painted and you have {paint_left} l paint left!")
    break
  
  elif total_paint == to_be_painted_sq_m:
    print("All walls are painted! Great job, Pesho!" )
    break
  
  command = input()

else:
  surface_left = to_be_painted_sq_m - total_paint
  print(f"{surface_left} quadratic m left." )
