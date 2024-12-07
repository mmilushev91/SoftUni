from math import ceil

people_count = int(input())
entry_price = float(input())
lounge_price = float(input())
umbrella_price = float(input())
        
lounge_count = ceil(people_count * 0.75)
umbrella_count = ceil(people_count / 2)

final_price = lounge_count * lounge_price + umbrella_count * umbrella_price + people_count * entry_price
print(f"{final_price:.2f} lv." )
