guests_count = int(input())
couvert_price = float(input())
budget = float(input())

if 10 <= guests_count <= 15:
  couvert_price -= couvert_price * 0.15 
elif 15 < guests_count <= 20:
  couvert_price -= couvert_price * 0.20 
elif guests_count > 20:
  couvert_price -= couvert_price * 0.25
  
cake_price = budget * 0.10

total_price = guests_count * couvert_price + cake_price

if budget >= total_price:
  money_left = budget - total_price
  
  print(f"It is party time! {money_left:.2f} leva left.")

else:
  money_needed = total_price - budget
  
  print(f"No party! {money_needed:.2f} leva needed.")
  
