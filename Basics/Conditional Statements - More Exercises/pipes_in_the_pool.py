pool_volume = int(input())

pipe_1_hourly = int(input())
pipe_2_hourly = int(input())

hours = float(input())

pipe_1_volume = pipe_1_hourly * hours
pipe_2_volume = pipe_2_hourly * hours

sum_pipes_volume = pipe_1_volume + pipe_2_volume

if pool_volume >= sum_pipes_volume:
  pool_volume_percent = (sum_pipes_volume / pool_volume) * 100
  pipe_1_volume_percent = (pipe_1_volume / sum_pipes_volume) * 100
  pipe_2_volume_percent = (pipe_2_volume / sum_pipes_volume) * 100
  
  print(f"The pool is {pool_volume_percent:.2f}% full. Pipe 1: {pipe_1_volume_percent:.2f}%. Pipe 2: {pipe_2_volume_percent:.2f}%.")

else:
  overflow = sum_pipes_volume - pool_volume
  
  print(f"For {hours} hours the pool overflows with {overflow:.2f} liters.")
  
