numbers_count = int(input())

max_number = float("-inf")
sum_numbers = 0

for _ in range(numbers_count):
    num = int(input())
    
    if max_number < num:
        max_number = num
    
    sum_numbers += num

sum_numbers -= max_number

if sum_numbers == max_number:
    print("Yes")
    print(f"Sum = {sum_numbers}")

else:
    difference = abs(sum_numbers - max_number)
    
    print("No")
    print(f"Diff = {difference}")
  
