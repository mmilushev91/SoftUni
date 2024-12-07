command = input()

max_points = float("-inf")
winner = None 

while command != "Stop":
  player_name = command
  
  player_points = 0
  
  for char in player_name:
    num = int(input())
    char_num = ord(char)
    
    if char_num == num:
      player_points += 10 
    else:
      player_points += 2 
    
  if max_points <= player_points:
    max_points = player_points
    winner = player_name
  
  command = input()

print(f"The winner is {winner} with {max_points} points!")
