prices = {
  "Espresso": {
    "Without": 0.90,
    "Normal": 1,
    "Extra": 1.20,
  },
  
  "Cappuccino": {
    "Without": 1,
    "Normal": 1.20,
    "Extra": 1.60,
  },

  "Tea": {
    "Without": 0.50,
    "Normal": 0.60,
    "Extra": 0.70,
  },
}

beverage = input()
suggar_type = input()
beverages_count = int(input())

price = prices[beverage][suggar_type] * beverages_count


if suggar_type == "Without":
  price *= 0.65

if beverage == "Espresso" and beverages_count >= 5:
  price *= 0.75

if price > 15:
  price *= 0.80

print(f"You bought {beverages_count} cups of {beverage} for {price:.2f} lv.")
