joinery_count = int(input())
joinery_type = input()
delivery = input()

single_price = 0

if joinery_count < 10:
  
  print("Invalid order")
  quit()

if joinery_type == "90X130":
  single_price = 110
  
  if joinery_count > 60:
    single_price *= 0.92
    
  elif joinery_count > 30:
    single_price *= 0.95

elif joinery_type == "100X150":
  single_price = 140
  
  if joinery_count > 80:
    single_price *= 0.90
    
  elif joinery_count > 40:
    single_price *= 0.94

elif joinery_type == "130X180":
  single_price = 190
  
  if joinery_count > 50:
    single_price *= 0.88
    
  elif joinery_count > 20:
    single_price *= 0.93 

elif joinery_type == "200X300":
  single_price = 250
  
  if joinery_count > 50:
    single_price *= 0.86
    
  elif joinery_count > 25:
    single_price *= 0.91 
  
final_price = single_price * joinery_count

if delivery == "With delivery":
  final_price += 60

if joinery_count > 99:
  final_price *= 0.96

print(f"{final_price:.2f} BGN")Aluminum Joinery
