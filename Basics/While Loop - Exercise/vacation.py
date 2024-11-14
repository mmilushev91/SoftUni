tour_price = float(input())
available_money = float(input())

spend_days = 0
days_counter = 0

while available_money < tour_price:
  action = input()
  money = float(input())
  
  days_counter += 1
  
  if action == "spend":
    spend_days += 1 
    
    if money > available_money:
        available_money = 0
    else:
        available_money -= money
    
    if spend_days == 5:
      print("You can't save the money.")
      print(f"{days_counter}")
      break
  else:
    spend_days = 0
    available_money += money

else:
  print(f"You saved the money for {days_counter} days.")
  
  
