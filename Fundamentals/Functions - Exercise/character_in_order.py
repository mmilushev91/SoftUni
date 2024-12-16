def print_ascii(start, end):
  for value in range(start, end):
    print(chr(value), end=" ")

input_start = ord(input()) + 1
input_end = ord(input())

print_ascii(input_start, input_end)
