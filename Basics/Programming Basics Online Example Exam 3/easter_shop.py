store_eggs = int(input())

command = input()

sold_eggs = 0

while command != "Close":
  
  action = command
  
  quantity = int(input())
  
  if action == "Buy":
    
    if quantity > store_eggs:

      print("Not enough eggs in store!")
      print(f"You can buy only {store_eggs}.")
      
      break
    
    store_eggs -= quantity
    sold_eggs += quantity
  
  elif action == "Fill":
    store_eggs += quantity

  command = input()

else:
  print("Store is closed!")
  print(f"{sold_eggs} eggs sold.")
