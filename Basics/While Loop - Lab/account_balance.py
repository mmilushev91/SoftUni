command = input()

account_money = 0

while command != "NoMoreMoney":
  amount = float(command)
  
  if amount < 0:
    print("Invalid operation!")
    break
  else:
    
    print(f"Increase: {amount:.2f}")
    account_money += amount
  
  command = input()

print(f"Total: {account_money:.2f}")
  
