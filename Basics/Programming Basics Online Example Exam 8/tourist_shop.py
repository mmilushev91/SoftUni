budget = float(input())

bought_products_count = 0
bought_products_price = 0

command = input()

while command != "Stop":

    product = command
    price = float(input())

    bought_products_count += 1

    if bought_products_count % 3 == 0:
        price *= 0.5

    if price > budget:
        money_needed = price - budget

        print("You don't have enough money!")
        print(f"You need {money_needed:.2f} leva!")

        break

    budget -= price
    bought_products_price += price

    command = input()

else:
    print(f"You bought {bought_products_count} products for {bought_products_price:.2f} leva.")
