apart_width = int(input())
apart_length = int(input())
apart_hight = int(input())

free_space = apart_width * apart_hight * apart_length

command = input()

while command != "Done":
  boxes = int(command)
  
  free_space -= boxes
  
  if free_space < 0:
    
    print(f"No more free space! You need {abs(free_space)} Cubic meters more.")
    break
  
  command = input()

else:
  print(f"{free_space} Cubic meters left.")
  
