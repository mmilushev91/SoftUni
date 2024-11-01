from math import floor, ceil

days = int(input())
left_food_kgs = int(input())

dog_food_per_day_kg = float(input())
cat_food_per_day_kg = float(input())
turtle_food_gr = float(input()) / 1000

food_needed = (dog_food_per_day_kg + cat_food_per_day_kg + turtle_food_gr) * days

if food_needed <= left_food_kgs:
  leftover_food = left_food_kgs - food_needed
  
  print(f"{floor(leftover_food)} kilos of food left.")

else:
  needed_food = food_needed - left_food_kgs

  print(f"{ceil(needed_food)} more kilos of food are needed.")
  
