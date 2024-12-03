best_player = None
best_player_goals = float("-inf")
has_a_hettrick = False

command = input()

while command !="END":
  player_name = command
  
  goals = int(input())
  
  if goals > best_player_goals:
    best_player_goals = goals
    best_player = player_name
    
    has_a_hettrick = False
    
    if goals >= 3:
      has_a_hettrick = True
  
  if goals >= 10:
    break
  command = input()

print(f"{best_player} is the best player!")

if has_a_hettrick:
  print(f"He has scored {best_player_goals} goals and made a hat-trick !!!")
else:
  print(f"He has scored {best_player_goals} goals.")
