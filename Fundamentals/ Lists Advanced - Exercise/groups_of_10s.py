from math import ceil

numbers = [int(num) for num in input().split(", ")]

max_number = max(numbers)
max_group = ceil(max_number / 10)

for group in range(1, max_group + 1):
  number_group = group * 10
  curent_group = [num for num in numbers if (number_group - 10) < num <= number_group]
  
  print(f"Group of {number_group}'s: {curent_group}")
