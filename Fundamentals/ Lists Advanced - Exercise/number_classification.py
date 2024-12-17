number_statistics = {
  "Positive": [],
  "Negative": [],
  "Even": [],
  "Odd": [],
}

numbers = [int(num) for num in input().split(", ")]

for num in numbers:
  if num >= 0:
    number_statistics["Positive"].append(num)
  else:
    number_statistics["Negative"].append(num)
  
  if num % 2 == 0:
    number_statistics["Even"].append(num)
  else:
    number_statistics["Odd"].append(num)

for key, value in number_statistics.items():
  print(f"{key}: {', '.join(str(num) for num in value)}")
  
