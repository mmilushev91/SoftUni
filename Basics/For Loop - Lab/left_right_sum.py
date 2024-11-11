numbers_count = int(input())

left_sum = sum([int(input()) for _ in range(numbers_count)])
right_sum = sum([int(input()) for _ in range(numbers_count)])

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}" )
    
else:
    difference = abs(left_sum - right_sum)
    
    print(f"No, diff = {difference}")
  
