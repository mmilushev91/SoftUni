from math import floor, ceil

WINE_FIELD = 0.40
GRAPE_PER_LITTER = 2.5

field_sq_m = int(input())
grape_per_sq_m = float(input())
required_wine_litters = int(input())
workers_count = int(input())

wine_field = field_sq_m * WINE_FIELD
grape_kg = wine_field * grape_per_sq_m
produced_wine = grape_kg / GRAPE_PER_LITTER

if produced_wine < required_wine_litters:
  needed_wine = required_wine_litters - produced_wine
  
  print(f"It will be a tough winter! More {floor(needed_wine)} liters wine needed.")

else:
  leftover_wine = produced_wine - required_wine_litters
  wine_per_worker = leftover_wine / workers_count
  
  print(f"Good harvest this year! Total wine: {floor(produced_wine)} liters.")
  print(f"{ceil(leftover_wine)} liters left -> {ceil(wine_per_worker)} liters per person.")
  
