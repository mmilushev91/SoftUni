def solve(num_list):
  
  return [min(num_list), max(num_list), sum(num_list)]

number_list = [int(num) for num in input().split()]

result = solve(number_list)

print(f"The minimum number is {result[0]}")
print(f"The maximum number is {result[1]}")
print(f"The sum number is: {result[2]}")
