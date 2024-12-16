n = int(input())

numbers_filters = {
  "even": [],
  "odd": [],
  "positive": [],
  "negative": [],
}

for _ in range(n):
  num = int(input())
  
  if num % 2 == 0:
    numbers_filters["even"].append(num)
  else:
    numbers_filters["odd"].append(num)
  
  if num >= 0:
    numbers_filters["positive"].append(num)
  else:
    numbers_filters["negative"].append(num)

command = input()

print(numbers_filters[command])
