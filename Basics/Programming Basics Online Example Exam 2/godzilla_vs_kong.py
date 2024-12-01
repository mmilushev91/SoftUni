budget = float(input())
statists_count = int(input())
statist_outfit_price = float(input())

if statists_count > 150:
    statist_outfit_price -= statist_outfit_price * 0.10

decor = budget * 0.10

total_price = statists_count * statist_outfit_price + decor

if total_price > budget:
    needed_money = total_price - budget

    print("Not enough money!")
    print(f"Wingard needs {needed_money:.2f} leva more.")

else:
    money_left = budget - total_price

    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")
