command = input()

currrent_money = 0

while command != "End":
  destination = command
  amount_needed = float(input())
  
  while currrent_money < amount_needed:
    saved_money = float(input())
    
    currrent_money += saved_money
  
  print(f"Going to {destination}!")
  
  currrent_money = 0
  
  command = input()
