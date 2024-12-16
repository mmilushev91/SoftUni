times_list = input().split(" ")

car_len = len(times_list) // 2
left_car_time = 0
for time in range(car_len):
  if int(times_list[time]) == 0:
    left_car_time *= 0.80
  else:
    left_car_time += int(times_list[time])

right_car_time  = 0 

for time in range(len(times_list) - 1, car_len, -1):
  if int(times_list[time]) == 0:
    right_car_time  *= 0.80
  else:
    right_car_time  += int(times_list[time])
    
winner = ""
if right_car_time < left_car_time:
  winner = "right"
  print(f"The winner is {winner} with total time: {right_car_time:.1f}")
else:
  winner = "left"
  print(f"The winner is {winner} with total time: {left_car_time:.1f}")
