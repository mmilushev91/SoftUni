substrings = input().split(", ")
strings = input().split(", ")

output = []

for substring in substrings:
  
  for string in strings:
    if substring in string and substring not in output:
      output.append(substring)

print(output)
