factor = int(input())
count = int(input())

number = factor

result = []

for _ in range(count):
  result.append(number)
  
  number += factor

print(result)
