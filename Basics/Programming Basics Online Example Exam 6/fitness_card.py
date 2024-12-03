fitness_card_prices = {
    "m": {
        "Gym": 42,
        "Boxing": 41,
        "Yoga": 45,
        "Zumba": 34,
        "Dances": 51,
        "Pilates": 39,
    },

    "f": {
        "Gym": 35,
        "Boxing": 37,
        "Yoga": 42,
        "Zumba": 31,
        "Dances": 53,
        "Pilates": 37,
    }
}

budget = float(input())
sex = input()
age = int(input())
sport = input()

card_price = fitness_card_prices[sex][sport]

if age <= 19:
    card_price *= 0.80

if budget >= card_price:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    money_needed = card_price - budget

    print(f"You don't have enough money! You need ${money_needed:.2f} more.")
