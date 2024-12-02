strawberry_price = float(input())
bananas_kg = float(input())
oranges_kg = float(input())
raspberries_kg = float(input())
strawberries_kg = float(input())

raspberries_price = strawberry_price * 0.50
oranges_price = raspberries_price * 0.60
bananas_price = raspberries_price * 0.20

bill = strawberries_kg * strawberry_price + bananas_kg * bananas_price + oranges_kg * oranges_price\
       + raspberries_kg * raspberries_price

print(f"{bill:.2f}")
