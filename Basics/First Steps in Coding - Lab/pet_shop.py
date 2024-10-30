DOG_PACKET_PRICE = 2.5
CAT_PACKET_PRICE = 4

dog_packets_count = int(input())
cat_packets_count = int(input())

dog_food_price = dog_packets_count * DOG_PACKET_PRICE
cat_food_price = cat_packets_count * CAT_PACKET_PRICE

total_price = dog_food_price + cat_food_price

print(f"{total_price} lv.")
