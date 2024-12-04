prices = {
  "Winter": {
    "Dubai": 45000,
    "Sofia": 17000,
    "London": 24000,
  },
  
  "Summer": {
    "Dubai": 40000,
    "Sofia": 12500,
    "London": 20250,
  },
}

budget = float(input())
destination = input()
season = input()
days_count = int(input())

daily_price = prices[season][destination]

if destination == "Dubai":
  daily_price *= 0.70
elif destination == "Sofia":
  daily_price *= 1.25

total_price = daily_price * days_count

if budget >= total_price:
  money_left = budget - total_price
  
  print(f"The budget for the movie is enough! We have {money_left:.2f} leva left!")

else:
  money_needed = total_price - budget
  print(f"The director needs {money_needed:.2f} leva more!")
