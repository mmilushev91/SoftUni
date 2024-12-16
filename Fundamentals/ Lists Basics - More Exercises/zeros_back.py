numbers = [int(num) for num in input().split(", ")]

zero_count = numbers.count(0)

for _ in range(zero_count):
  numbers.remove(0)
  numbers.append(0)

print(numbers)
