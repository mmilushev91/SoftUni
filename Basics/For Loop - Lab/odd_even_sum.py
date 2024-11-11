numbers_count = int(input())

even_sum, odd_sum = 0, 0

for index in range(numbers_count):
    num = int(input())
    
    if index % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

if even_sum == odd_sum:
    print("Yes")
    print(f"Sum = {even_sum}")

else:
    difference = abs(even_sum - odd_sum)
    
    print("No")
    print(f"Diff = {difference}")
