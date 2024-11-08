FLOWER_PRICES = {
    
    "Summer": {
        "chrysanthemums": 2,
        "roses": 4.10,
        "tulips": 2.50,
    },
    
    "Spring": {
        "chrysanthemums": 2,
        "roses": 4.10,
        "tulips": 2.50,
    },
    
    "Autumn": {
        "chrysanthemums": 3.75,
        "roses": 4.50,
        "tulips": 4.15,
    },
    
    "Winter": {
        "chrysanthemums": 3.75,
        "roses": 4.50,
        "tulips": 4.15,
    },
}

counts = [int(input()), int(input()), int(input())]
season = input()
is_it_a_holiday = input()

season_prices = FLOWER_PRICES[season]

prices = []
index = 0

for item in season_prices:
    prices.append(season_prices[item] * counts[index])
    
    index += 1

total_price = sum(prices)

if is_it_a_holiday == "Y":
    total_price += total_price * 0.15

if season == "Spring" and counts[2] > 7:
    total_price -= total_price * 0.05

elif season == "Winter" and counts[1] >= 10:
    total_price -= total_price * 0.10

if sum(counts) > 20:
    total_price -= total_price * 0.20

final_price = total_price + 2

print(f"{final_price:.2f}")
