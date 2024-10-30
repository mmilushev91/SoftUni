  PERCENT = 0.10

budget = float(input())
statists_count = int(input())
statist_outfit = float(input())

decor = budget * PERCENT

if statists_count > 150:
  statist_outfit -= statist_outfit * PERCENT

total_cost = statists_count * statist_outfit + decor

if total_cost <= budget:
  money_left = budget - total_cost
  
  print("Action!")
  print(f"Wingard starts filming with {money_left:.2f} leva left.")
else:
  money_needed = total_cost - budget
  
  print("Not enough money!")
  print(f"Wingard needs {money_needed:.2f} leva more.")
