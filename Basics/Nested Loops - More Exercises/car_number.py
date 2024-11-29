start = int(input())
end = int(input()) + 1
      
for num1 in range(start, end):
  for num2 in range(start, end):
    for num3 in range(start, end):
      for num4 in range(start, end):

        if num1 % 2 == 0 and num4 % 2 == 0:
          continue
        
        
        if num1 % 2 != 0 and num4 % 2 != 0:
          continue
        
        if num1 < num4:
          continue
        
        if (num2 + num3) % 2 != 0:
          continue
        
        print(f"{num1}{num2}{num3}{num4}", end=" ")
