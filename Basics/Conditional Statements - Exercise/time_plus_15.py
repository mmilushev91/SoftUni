ADDED_MINUTES = 15

hours = int(input())
minutes = int(input()) + ADDED_MINUTES

if minutes > 59:
  minutes = minutes % 60
  hours += 1
  
  if hours > 23:
    hours = 0

print(hours, end=":")

if minutes < 10:
  print(f"0{minutes}")
else:
  print(minutes)
  
