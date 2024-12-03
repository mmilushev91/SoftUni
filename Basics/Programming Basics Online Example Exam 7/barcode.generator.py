start = str(int(input()))
end = str(int(input()))

start_1 = int(start[0])
start_2 = int(start[1])
start_3 = int(start[2])
start_4 = int(start[3])

end_1 = int(end[0]) + 1
end_2 = int(end[1]) + 1
end_3 = int(end[2]) + 1
end_4 = int(end[3]) + 1

for num1 in range(start_1, end_1):
  
  if num1 % 2 == 0:
    continue
  
  for num2 in range(start_2, end_2):
  
    if num2 % 2 == 0:
      continue
  
    for num3 in range(start_3, end_3):
    
      if num3 % 2 == 0:
        continue
    
      for num4 in range(start_4, end_4):
    
        if num4 % 2 == 0:
          continue
        
        print(f"{num1}{num2}{num3}{num4}", end=" ")
        
