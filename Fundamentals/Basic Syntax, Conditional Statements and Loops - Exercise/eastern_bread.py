budget = float(input())
flour_price = float(input())

eggs_price = flour_price * 0.75
milk_price = (flour_price + flour_price * 0.25) / 4

loaf_price = flour_price + eggs_price + milk_price

loaves_count = 0
colored_eggs = 0

while budget >= loaf_price:
    loaves_count += 1
    colored_eggs += 3

    if loaves_count % 3 == 0:
        colored_eggs -= loaves_count - 2

    budget -= loaf_price

print(f"You made {loaves_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
