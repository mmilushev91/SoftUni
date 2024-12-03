days_count = int(input()) + 1
hours_count = int(input()) + 1

total_bill = 0

for day in range(1, days_count):
  
  daily_bill = 0
  
  for hour in range(1, hours_count):
    
    if day % 2 == 0 and hour % 2 != 0:
      daily_bill += 2.50
    elif day % 2 != 0 and hour % 2 == 0:
      daily_bill += 1.25
    else:
      daily_bill += 1 
  
  print(f"Day: {day} - {daily_bill:.2f} leva")
  
  total_bill += daily_bill

print(f"Total: {total_bill:.2f} leva")
