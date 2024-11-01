FUEL_PRICES = {
  "Gas": 0.93,
  "Diesel": 2.33,
  "Gasoline": 2.22,
}

FUEL_CARD_DISCOUNTS = {
  "Gas": 0.08,
  "Diesel": 0.12,
  "Gasoline": 0.18,
}

FUELING_DISCOUNT_FIRST_LEVEL = 0.08
FUELING_DISCOUNT_SECOND_LEVEL = 0.10

FIRST_LEVEL_LOW_LIMIT = 20
FIRST_LEVEL_HIGH_LIMIT = 25

fuel_type = input()
fuel_quantity = float(input())
card = input()

fuel_cost_litter = FUEL_PRICES[fuel_type]

if card == "Yes":
  fuel_cost_litter -= FUEL_CARD_DISCOUNTS[fuel_type]

if FIRST_LEVEL_LOW_LIMIT <= fuel_quantity <= FIRST_LEVEL_HIGH_LIMIT:
  fuel_cost_litter -= fuel_cost_litter * FUELING_DISCOUNT_FIRST_LEVEL
  
elif fuel_quantity > FIRST_LEVEL_HIGH_LIMIT:
  fuel_cost_litter -= fuel_cost_litter * FUELING_DISCOUNT_SECOND_LEVEL

final_cost = fuel_cost_litter * fuel_quantity

print(f"{final_cost:.2f} lv.")
