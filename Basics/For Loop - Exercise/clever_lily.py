age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

even_year_money = 0
gathered_money = 0

for year in range(1, age + 1):
    
    if year % 2 != 0:
        
        gathered_money += toy_price
    else:
        even_year_money += 10
        gathered_money += even_year_money - 1

if gathered_money >= washing_machine_price:
    money_left = gathered_money - washing_machine_price
    
    print(f"Yes! {money_left:.2f}" )
else:
    money_needed = washing_machine_price - gathered_money
    
    print(f"No! {money_needed:.2f}")
  
