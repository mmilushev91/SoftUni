def remove_min_num(numbers):

  min_num = float("inf")
  
  for num in numbers:
    
    if min_num > num:
      min_num = num

  numbers.remove(min_num)
  
numbers = [int(num) for num in input().split()]
numbers_to_remove = int(input())


for _ in range(numbers_to_remove):
  remove_min_num(numbers)

print(', '.join(str(num) for num in numbers))
