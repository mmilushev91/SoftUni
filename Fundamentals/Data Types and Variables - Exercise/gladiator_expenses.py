lost_fights_count = int(input()) + 1
helmtet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_cost = 0
shield_break_counter = 0

for lost_fight_num in range(1, lost_fights_count):
  
  if lost_fight_num % 2 == 0:
    total_cost += helmtet_price
  
  if lost_fight_num % 3 == 0:
    total_cost += sword_price
    
    if lost_fight_num % 2 == 0:
      total_cost += shield_price
      shield_break_counter += 1 
      
      if shield_break_counter == 2:
        total_cost += armor_price
        shield_break_counter = 0

print(f"Gladiator expenses: {total_cost:.2f} aureus")
