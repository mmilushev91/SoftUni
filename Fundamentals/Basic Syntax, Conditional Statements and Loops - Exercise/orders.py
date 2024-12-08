orders_count = int(input())

total_price = 0

for _ in range(orders_count):
    capsule_price = float(input())
    days = int(input())
    capsules_count = int(input())

    if capsule_price < 0.01 or capsule_price > 100:
        continue

    if days not in range(1, 32):
        continue

    if capsules_count not in range(1, 2001):
        continue

    order_price = capsule_price * capsules_count * days

    print(f"The price for the coffee is: ${order_price:.2f}")

    total_price += order_price

print(f"Total: ${total_price:.2f}")
