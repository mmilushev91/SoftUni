n = int(input())

start = 97
end = start + n

for char1 in range(start, end):
  for char2 in range(start, end):
    for char3 in range(start, end):
      print(f"{chr(char1)}{chr(char2)}{chr(char3)}")
