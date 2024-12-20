string = input()

digits = []
non_digits = []

for char in string:
  if char.isdigit():
    digits.append(int(char))
  else:
    non_digits.append(char)

take_list = []
skip_list = []

for i in range(len(digits)):
  if i % 2 == 0:
    take_list.append(digits[i])
  else:
    skip_list.append(digits[i])
    
start = 0
end = 0
result = ""
  
for i in range(len(take_list)):
  start = end
  
  end += take_list[i]
  
  result += ''.join(non_digits[start:end])
  
  start = end 
  end += skip_list[i]

print(result)
