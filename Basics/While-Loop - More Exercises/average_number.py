n = int(input())

sum_nums = 0

for _ in range(n):
  num = int(input())
  
  sum_nums += num

average = sum_nums / n 

print(f"{average:.2f}")
