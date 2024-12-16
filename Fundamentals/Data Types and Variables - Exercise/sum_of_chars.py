n = int(input())

ascii_sum = 0

for _ in range(n):
  char = input()
  
  ascii_sum += ord(char)

print(f"The sum equals: {ascii_sum}")
