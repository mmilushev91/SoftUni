wagons_count = int(input())

wagons = [0] * wagons_count

command = input()

while command != "End":
  command_line = command.split()
  
  action = command_line[0]
  
  if action == "add":
    people_count = int(command_line[1])
    wagons[-1] += people_count
  
  else:
    index = int(command_line[1])
    people_count = int(command_line[2])
    
    if action == "insert":
      
      wagons[index] += people_count
    
    else:
      wagons[index] -= people_count
  
  command = input()

print(wagons)
