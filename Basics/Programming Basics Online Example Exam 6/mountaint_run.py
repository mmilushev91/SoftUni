record_to_beat = float(input())
distance = float(input())
time_per_m = float(input())

slow_time = int(distance / 50) * 30

total_time = distance * time_per_m + slow_time

if record_to_beat > total_time:
  print(f" Yes! The new record is {total_time:.2f} seconds.")
else:
  time_needed = total_time - record_to_beat
  print(f"No! He was {time_needed:.2f} seconds slower.")
