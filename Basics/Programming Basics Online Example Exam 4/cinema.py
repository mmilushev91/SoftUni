hall_capacity = int(input())

command = input()

money_earned = 0

while command != "Movie time!":
  visitors_count = int(command)
  
  if visitors_count > hall_capacity:
    print("The cinema is full.")
    break
  
  hall_capacity -= visitors_count
  
  money_earned += visitors_count * 5
  
  if visitors_count % 3 == 0:
    money_earned -= 5 
  
  command = input()

else:
  print(f"There are {hall_capacity} seats left in the cinema.")
