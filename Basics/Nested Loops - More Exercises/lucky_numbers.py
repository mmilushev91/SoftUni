n = int(input())

for num1 in range(1, 10):
  for num2 in range(1, 10):
    for num3 in range(1, 10):
      for num4 in range(1, 10):
        
        first_pair = num1 + num2
        second_pair = num3 + num4
        
        if second_pair != first_pair:
          continue
        
        if n % second_pair != 0:
          continue
        
        print(f"{num1}{num2}{num3}{num4}", end=" ")
