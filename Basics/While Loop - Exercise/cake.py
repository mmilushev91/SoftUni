cake_width = int(input())
cake_length = int(input())

cake_pcs = cake_width * cake_length

command = input()

while command != "STOP":
  taken_pcs = int(command)
  
  cake_pcs -= taken_pcs
  
  if cake_pcs < 0:
    
    print(f"No more cake left! You need {abs(cake_pcs)} pieces more.")
    break
  
  command = input()

else:
  print(f"{cake_pcs} pieces are left." )
