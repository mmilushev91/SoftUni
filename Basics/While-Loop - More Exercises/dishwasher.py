DETERGENT_PER_BOTTLE = 750
DETERGENT_FOR_PLATE = 5
DETERGENT_FOR_POTS = 15

detergent_bottles = int(input())

total_detergent_ml = detergent_bottles * DETERGENT_PER_BOTTLE

washed_plates = 0 
washed_pots = 0
counter = 0

command = input()

while command != "End":
  dishes = int(command)
  
  counter += 1
  
  detergent_used = 0
  
  if counter % 3 == 0:
    detergent_used = dishes * DETERGENT_FOR_POTS
    washed_pots += dishes
  else:
    detergent_used = dishes * DETERGENT_FOR_PLATE
    washed_plates += dishes
  
  total_detergent_ml -= detergent_used
  
  if total_detergent_ml < 0:
    print(f"Not enough detergent, {abs(total_detergent_ml)} ml. more necessary!")
    break
  
  command = input()

else:
  print("Detergent was enough!")
  print(f"{washed_plates} dishes and {washed_pots} pots were washed.")
  print(f"Leftover detergent {total_detergent_ml} ml.")
