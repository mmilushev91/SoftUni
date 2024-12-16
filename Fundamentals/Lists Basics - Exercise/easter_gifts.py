gifts = input().split()

command = input()

while command != "No Money":
  command_line = command.split()
  
  command_word = command_line[0]
  gift = command_line[1]
  
  
  if command_word == "OutOfStock":
    
    for index in range(len(gifts)):
      
      if gifts[index] == gift:
        gifts[index] = None
        
  elif command_word == "Required":
    index = int(command_line[2])
    
    if 0 <= index < len(gifts):
    
      gifts[index] = gift
  
  else:
    gifts[len(gifts) - 1] = gift
  
  command = input()

print(' '.join(gift for gift in gifts if gift != None))
