LOW_LIMIT = 100
HIGH_LIMIT = 200

num = int(input())

if num < LOW_LIMIT:
  print("Less than 100")
elif num <= HIGH_LIMIT:
  print("Between 100 and 200")
else:
  print("Greater than 200")
