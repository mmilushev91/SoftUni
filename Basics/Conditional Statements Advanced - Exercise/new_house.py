FLOWERS_PRICES = {
    "Roses": 5.00,
    "Dahlias": 3.80,
    "Tulips": 2.80,
    "Narcissus": 3,
    "Gladiolus": 2.50,
}

FLOWERS_COUNTS_FOR_PRICE = [80, 90, 120]
FLOWERS_PERCENTS_FOR_PRICE = [0.10, 0.150, 0.20]
FLOWER_TYPES = ["Roses", "Dahlias", "Tulips", "Narcissus","Gladiolus"]

flowers_type = input()
flowers_count = int(input())
budget = int(input())

flower_price = FLOWERS_PRICES[flowers_type]
total_price = flower_price * flowers_count

if flowers_type == FLOWER_TYPES[0] \
    and flowers_count > FLOWERS_COUNTS_FOR_PRICE[0]:
        total_price -= total_price * FLOWERS_PERCENTS_FOR_PRICE[0]

elif flowers_type == FLOWER_TYPES[1] and flowers_count > FLOWERS_COUNTS_FOR_PRICE[1]:
    total_price -= total_price * FLOWERS_PERCENTS_FOR_PRICE[1]

elif flowers_type == FLOWER_TYPES[2] and flowers_count > FLOWERS_COUNTS_FOR_PRICE[0]:
    total_price -= total_price * FLOWERS_PERCENTS_FOR_PRICE[1]

elif flowers_type == FLOWER_TYPES[3] and flowers_count < FLOWERS_COUNTS_FOR_PRICE[2]:
    total_price += total_price * FLOWERS_PERCENTS_FOR_PRICE[1]

elif flowers_type == FLOWER_TYPES[4] and flowers_count < FLOWERS_COUNTS_FOR_PRICE[0]:
    total_price += total_price * FLOWERS_PERCENTS_FOR_PRICE[2]

if total_price <= budget:
    money_left = budget - total_price
    
    print(f"Hey, you have a great garden with {flowers_count} {flowers_type} and {money_left:.2f} leva left.")
else:
    money_needed = total_price - budget
    
    print(f"Not enough money, you need {money_needed:.2f} leva more.")
  
