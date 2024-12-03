products_prices = {
  "small": {
    "Watermelon": 112,
    "Mango": 73.32,
    "Pineapple": 84.20,
    "Raspberry": 40,
  },
  
  "big": {
    "Watermelon": 143.5,
    "Mango": 98,
    "Pineapple": 124,
    "Raspberry": 76,
  },
  
}

fruit = input()
set_size = input()
sets_count = int(input())

price = products_prices[set_size][fruit] * sets_count

if 400 <= price <= 1000:
  price *= 0.85
elif price > 1000:
  price *= 0.50

print(f"{price:.2f} lv.")
