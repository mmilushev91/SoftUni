first = int(input())
second = int(input())
third = int(input())

sum_time = first + second + third

minutes = sum_time // 60
seconds = sum_time % 60

print(minutes, end=":")

if seconds < 10:
  print(f"0{seconds}")
else:
  print(seconds)
  
