rooms = int(input())

enough_rooms = True
total_free_chairs = 0

for room_number in range(1, rooms + 1):
  chairs, visitors = input().split()
  chairs_count = len(chairs)
  visitors_count = int(visitors)
  
  if chairs_count < visitors_count:
    
    print(f"{visitors_count - chairs_count} more chairs needed in room {room_number}")
    enough_rooms = False
  
  else:
    total_free_chairs += chairs_count - visitors_count

if enough_rooms:
  print(f"Game On, {total_free_chairs} free chairs left")
