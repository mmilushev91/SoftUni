discounts = {
    "Saturday": 0.90,
    "Sunday": 0.80,
}

budget = float(input())
fuel = float(input())
day = input()

fuel_price = fuel * 2.10

cost = fuel_price + 100

cost *= discounts[day]

if budget >= cost:
    money_left = budget - cost

    print(f"Safari time! Money left: {money_left:.2f} lv. ")

else:
    money_needed = cost - budget

    print(f"Not enough money! Money needed: {money_needed:.2f} lv.")
