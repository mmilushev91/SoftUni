TICKET_PRICE = 150

products = input().split("|")
budget = float(input())

max_prices = {
  "Clothes": 50,
  "Shoes": 35,
  "Accessories": 20.50,
}

bought_product_prices = []
profit = 0

for product in products:
  product_name, product_price = product.split("->")
  product_price = float(product_price)
  
  if product_price <= max_prices[product_name]:
    
    if product_price <= budget:
      budget -= product_price
      
      sold_value = product_price * 1.4
      
      profit += sold_value - product_price
      
      bought_product_prices.append(sold_value)
      
print(' '.join(f"{price:.2f}" for price in bought_product_prices))
print(f"Profit: {profit:.2f}")

total_money = sum(bought_product_prices) + budget

if total_money >= TICKET_PRICE:
  print("Hello, France!")
else:
  print("Not enough money.")
