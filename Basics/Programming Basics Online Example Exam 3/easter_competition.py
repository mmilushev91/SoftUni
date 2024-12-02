easter_cakes_count = int(input())

winner_grade = float("-inf")
winner_name = None 

for _ in range(easter_cakes_count):
  chef_name = input()
  
  command = input()
  
  chef_total_grade = 0
  
  while command != "Stop":
    grade = int(command)
    
    chef_total_grade += grade
    
    command = input()
  
  print(f"{chef_name} has {chef_total_grade} points.")
  
  if winner_grade < chef_total_grade:
    winner_grade = chef_total_grade
    winner_name = chef_name
    
    print(f"{chef_name} is the new number 1!")
  
print(f"{winner_name} won competition with {winner_grade} points!")
