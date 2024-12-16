group_size = int(input())
days = int(input()) + 1 

coins = 0

for day_number in range(1, days):
  
  if day_number % 10 == 0:
    group_size -= 2
  
  if day_number % 15 == 0:
    group_size += 5
  
  coins += 50
  coins -= group_size * 2
  
  
  if day_number % 3 == 0:
    coins -= group_size * 3 
  
