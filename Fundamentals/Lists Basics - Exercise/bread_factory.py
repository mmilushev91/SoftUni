line = input().split("|")

energy = 100
coins = 100

for item in line:
  part, value = item.split("-")
  value = int(value)
  
  if part == "rest":
    
    energy_gained = 0 
    
    if energy + value <= 100:
      energy_gained = value
    else:
      energy_gained = 100 - energy
    
    energy += energy_gained
    
    print(f"You gained {energy_gained} energy.")
    print(f"Current energy: {energy}.")
  
  elif part == "order":
    
    
    if energy - 30 < 0:
      energy += 50
      
      print("You had to rest!")
      
      continue
    
    else:
      energy -= 30
      coins += value
      
      print(f"You earned {value} coins.")
  
  else:

    if value > coins:
      print(f"Closed! Cannot afford {part}.")
      break
    else:
      coins -= value
      print(f"You bought {part}.")

else:
  print("Day completed!")
  print(f"Coins: {coins}")
  print(f"Energy: {energy}")
