money_to_gather = int(input())

counter = 0
cash_paid_counter, card_paid_counter = 0, 0
cash_paid_amount, card_paid_amount = 0, 0

while True:
  command = input()
  
  if command == "End":
    print("Failed to collect required money for charity.")
    break
  
  amount = int(command)
  
  counter += 1
  
  if counter % 2 != 0:
  
    if amount > 100:
    
      print("Error in transaction!")
      continue
    
    else:
      cash_paid_counter += 1 
      cash_paid_amount += amount
      
      print("Product sold!")
  
  else:
    
    if amount < 10:
      print("Error in transaction!")
      continue
    
    else:
      card_paid_counter += 1 
      card_paid_amount += amount
      
      print("Product sold!")
  
  money_to_gather -= amount

  if money_to_gather <= 0:
    avg_cs = cash_paid_amount / cash_paid_counter
    avg_cc = card_paid_amount / card_paid_counter
    
    print(f"Average CS: {avg_cs:.2f}")
    print(f"Average CC: {avg_cc:.2f}" )
    
    break
