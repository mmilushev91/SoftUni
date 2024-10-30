DELAY_DISTANCE = 15
DELAY_TIME = 12.5

record = float(input())
distance = float(input())
time_per_m = float(input())

delay_time = (distance // 15) * 12.5

time = distance * time_per_m + delay_time

if time < record:
  print(f"Yes, he succeeded! The new world record is {time:.2f} seconds.")
else:
  time_slower = time - record
  
  print(f"No, he failed! He was {time_slower:.2f} seconds slower.")
  
