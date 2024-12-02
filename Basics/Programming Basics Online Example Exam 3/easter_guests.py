from math import ceil

guest_count = int(input())
budget = int(input())

easter_cake_count = ceil(guest_count / 3)
eggs_count = guest_count * 2

total_price = easter_cake_count * 4 + eggs_count * 0.45

if budget>= total_price:
  money_left = budget - total_price
  
  print(f"Lyubo bought {easter_cake_count} Easter bread and {eggs_count} eggs.")
  print(f"He has {money_left:.2f} lv. left.")

else:
  money_needed = total_price - budget
  
  print("Lyubo doesn't have enough money.")
