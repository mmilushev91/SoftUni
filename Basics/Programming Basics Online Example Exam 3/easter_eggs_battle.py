player_one_eggs = int(input())
player_two_eggs = int(input())

command = input()

while command != "End":
  winner = command

  if winner == "one":
    player_two_eggs -= 1 
  
  elif winner == "two":
    player_one_eggs -= 1
  
  if player_one_eggs == 0:
    
    print(f"Player one is out of eggs. Player two has {player_two_eggs} eggs left.")
    break
  
  if player_two_eggs == 0:
    print(f"Player two is out of eggs. Player one has {player_one_eggs} eggs left.")
    break
  
  command = input()
  
else:
  print(f"Player one has {player_one_eggs} eggs left.")
  
