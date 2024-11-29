days = int(input()) + 1
hours = int(input()) + 1

total_cost = 0 

for day in range(1, days):
  daily_tax = 0
  
  for hour in range(1, hours):
    
    if day % 2 == 0 and hour % 2 != 0:
      daily_tax += 2.50
    
    elif day % 2 != 0 and hour % 2 == 0:
      daily_tax += 1.25
    
    else:
      daily_tax += 1
  
  print(f"Day: {day} - {daily_tax:.2f} leva")
  
  total_cost += daily_tax

print(f"Total: {total_cost:.2f} leva")
