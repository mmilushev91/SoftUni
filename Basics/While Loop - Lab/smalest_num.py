command = input()

smalest_num = float("inf")

while command != "Stop":
  num = int(command)
  
  if num < smalest_num:
    smalest_num = num
  
  command = input()

print(smalest_num)
