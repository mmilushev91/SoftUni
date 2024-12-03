single_luggage_price = float(input())
luggage_kgs = float(input())
days = int(input())
luggage_count = int(input())

if luggage_kgs < 10:
  single_luggage_price *= 0.20
elif luggage_kgs <= 20:
  single_luggage_price *= 0.50

if days < 7:
  single_luggage_price *= 1.40
elif days <= 30:
  single_luggage_price *= 1.15
else:
  single_luggage_price *= 1.10

final_luggage_price = single_luggage_price * luggage_count

print(f"The total price of bags is: {final_luggage_price:.2f} lv. ")
