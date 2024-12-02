easter_decoration_prices = {
  "basket": 1.5,
  "wreath": 3.8,
  "chocolate bunny": 7,
}

custmomers_count = int(input()) 

total_income = 0

for custmomer in range(custmomers_count):
  
  command = input()
  
  customer_bil = 0
  purchases_count = 0
  
  while command != "Finish":
    purchase = command
    
    customer_bil += easter_decoration_prices[purchase]
    purchases_count += 1
    
    command = input()
  
  if purchases_count % 2 == 0:
    customer_bil -= customer_bil * 0.20
    
  print(f"You purchased {purchases_count} items for {customer_bil:.2f} leva.")
  
  total_income += customer_bil

print(f"Average bill per client is: {total_income / custmomers_count:.2f} leva.")
