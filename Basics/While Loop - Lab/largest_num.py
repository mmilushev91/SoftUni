command = input()

largest_num = float("-inf")

while command != "Stop":
  num = int(command)
  
  if num > largest_num:
    largest_num = num

  
  command = input()

print(largest_num)
