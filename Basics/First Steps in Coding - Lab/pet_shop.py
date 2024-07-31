# Pseudocode

# prompt user for number of dog and cat food packets
# init const variables for dog and cat packet price
# calculate dog price, cat price and total price
# print f string: "{крайната сума} lv."

dog_packets_count = int(input())
cat_packets_count = int(input())

DOG_PACKET_PRICE = 2.5
CAT_PACKET_PRICE = 4

dog_food_price = dog_packets_count * DOG_PACKET_PRICE
cat_food_price = cat_packets_count * CAT_PACKET_PRICE

total_price = dog_food_price + cat_food_price

print(f"{total_price} lv.")
