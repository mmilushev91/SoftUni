voucher_price = int(input())

tickets_bought = 0
others_bought = 0
purchase_price = 0

command = input()

while command != "End":
    purchase = command

    is_it_ticket = False

    if len(purchase) > 8:
        purchase_price = ord(purchase[0]) + ord(purchase[1])
        is_it_ticket = True
    else:
        purchase_price = ord(purchase[0])

    if purchase_price > voucher_price:
        break

    voucher_price -= purchase_price

    if is_it_ticket:
        tickets_bought += 1
    else:
        others_bought += 1

    command = input()

print(tickets_bought)
print(others_bought)
