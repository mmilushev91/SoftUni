discounts = {
    "Thrones": 0.50,
    "Lucifer": 0.40,
    "Protector": 0.30,
    "TotalDrama": 0.20,
    "Area": 0.10,
}

budget = float(input())
series_count = int(input())

total_series_price = 0

for _ in range(series_count):
    series_name = input()
    series_price = float(input())

    if series_name in discounts:
        series_price = series_price - series_price * discounts[series_name]

    total_series_price += series_price

if budget >= total_series_price:
    left_money = budget - total_series_price

    print(f"You bought all the series and left with {left_money:.2f} lv.")

else:
    money_needed = total_series_price - budget

    print(f"You need {money_needed:.2f} lv. more to buy the series!")
  
