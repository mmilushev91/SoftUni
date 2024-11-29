from math import ceil, floor

racks_price = float(input())

racks_count = int(input())
sneakers_count = int(input())


sneakers_price = racks_price / 6 

price = racks_count * racks_price + sneakers_count * sneakers_price
other_equipment = price * 0.20

total_price = price + other_equipment

djokovic_share = floor(total_price / 8)
sponsors_share = ceil(total_price * 0.875)

print(f"Price to be paid by Djokovic {djokovic_share}")
print(f"Price to be paid by sponsors {sponsors_share}")
