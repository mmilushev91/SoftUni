BONITO_PERCENT = 0.6
HORSE_MACKEREL_PERCENT= 0.80

MUSSELS_KG_PRICE = 7.50

mackerel_price_kg = float(input())
squirt_price_kg = float(input())

bonito_kgs = float(input())
horse_mackerel_kgs = float(input())
mussels_kgs = int(input())

bonito_price = mackerel_price_kg + (mackerel_price_kg * BONITO_PERCENT)
horse_mackerel_price = squirt_price_kg + (squirt_price_kg * HORSE_MACKEREL_PERCENT)

total_cost = (bonito_kgs * bonito_price) + (horse_mackerel_kgs * horse_mackerel_price) + (mussels_kgs * MUSSELS_KG_PRICE)

print(f"{total_cost:.2f}")

