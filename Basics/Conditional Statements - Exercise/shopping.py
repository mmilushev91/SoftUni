VIDEO_CARD = 250
PROCESSOR = 0.35
RAM = 0.10
DISCOUNT = 0.15

budget = float(input())

video_cards_count = int(input())
processors_count = int(input())
ram_count = int(input())

video_cards = video_cards_count * VIDEO_CARD
processors = processors_count * (PROCESSOR * video_cards)
ram = (RAM * video_cards) * ram_count

total_cost = video_cards + processors + ram

if video_cards_count > processors_count:
  total_cost -= total_cost * DISCOUNT

if budget >= total_cost:
  money_left = budget - total_cost
  
  print(f"You have {money_left:.2f} leva left!")
  
else:
  needed_money = total_cost - budget

  print(f"Not enough money! You need {needed_money:.2f} leva more!")
