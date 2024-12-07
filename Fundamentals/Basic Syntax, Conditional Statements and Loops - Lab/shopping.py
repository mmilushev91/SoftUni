budget = int(input())

command = input()

while command != "End":
    product_price = int(command)

    if product_price > budget:
        print("You went in overdraft!")
        break

    budget -= product_price

    command = input()

else:
    print("You bought everything needed.")
