budget = float(input())
nights_count = int(input())
night_price = float(input())
other_costs_percent = float(input()) / 100

if nights_count > 7:
  night_price *= 0.95

nights_price = nights_count * night_price 
other_costs_price = budget * other_costs_percent

total_price = nights_price + other_costs_price

if budget >= total_price:
  money_left = budget - total_price
  
  print(f"Ivanovi will be left with {money_left:.2f} leva after vacation.")

else:
  money_needed = total_price - budget
  
  print(f"{money_needed:.2f} leva needed.")
