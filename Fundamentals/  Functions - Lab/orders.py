def orders(order, quantity):
  
  order_prices = {
    "coffee": 1.50,
    "water": 1.00,
    "coke": 1.40,
    "snacks": 2.00
  }

  return f"{order_prices[order] * quantity:.2f}"

input_order = input()
input_quantity = int(input())

print(orders(input_order, input_quantity))
