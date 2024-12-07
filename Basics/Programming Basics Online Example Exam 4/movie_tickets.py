a1 = int(input())
a2 = int(input())
n = int(input())

for ascii_num in range(a1, a2):
  
  if ascii_num % 2 == 0:
    continue
  
  for num1 in range(1, n):
    for num2 in range(1, int(n / 2)):
      
      if (num1 + num2 + ascii_num) % 2 == 0:
        continue
      
      print(f"{chr(ascii_num)}-{num1}{num2}{ascii_num}")
