floors = int(input())
rooms = int(input())

for floor in range(floors, 0, -1):
  
  for room in range(0, rooms):

    room_type_letter = ""
    
    if floor == floors:
      room_type_letter = "L"
    elif floor % 2 != 0:
      room_type_letter = "A"
    else:
      room_type_letter = "O"
    
    print(f"{room_type_letter}{floor}{room}", end=" ")
  
  print()
  
