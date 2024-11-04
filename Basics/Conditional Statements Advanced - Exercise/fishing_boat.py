RENT_BOAT_PRICES = {
    "Spring": 3000 , 
    "Summer": 4200, 
    "Autumn": 4200,
    "Winter": 2600,
}

DISCOUNT_PERCENTS = [0.05, 0.10, 0.15, 0.25]
GROUP_COUNTS = [6, 11]

NO_ADDED_DISCOUNT = "Autumn"

budget = int(input())
season = input()
fisherman_count = int(input())

boat_price = RENT_BOAT_PRICES[season]

if fisherman_count <= GROUP_COUNTS[0]:
    boat_price -= boat_price * DISCOUNT_PERCENTS[1]
elif fisherman_count <= GROUP_COUNTS[1]:
    boat_price -= boat_price * DISCOUNT_PERCENTS[2]
else:
    boat_price -= boat_price * DISCOUNT_PERCENTS[3]

if fisherman_count % 2 == 0 and season != NO_ADDED_DISCOUNT:
    boat_price -= boat_price * DISCOUNT_PERCENTS[0]

if budget >= boat_price:
    money_left = budget - boat_price
    
    print(f"Yes! You have {money_left:.2f} leva left.")

else:
    money_needed = boat_price - budget
    
    print(f"Not enough money! You need {money_needed:.2f} leva.")
  
