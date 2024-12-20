ships = [[int(index) for index in input().split()] for _ in range(int(input()))]
positions = input().split()

destroyed_ships = 0

for position in positions:
  position_cordinates = position.split("-")
  
  row = int(position_cordinates[0])
  col = int(position_cordinates[1])
  
  if ships[row][col] > 0:
    ships[row][col] -= 1 
    
    if ships[row][col] == 0:
      destroyed_ships += 1 

print(destroyed_ships)
