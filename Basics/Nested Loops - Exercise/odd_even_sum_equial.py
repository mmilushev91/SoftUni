start = int(input())
end = int(input())
    
for num in range(start, end + 1):
  
  string_num = str(num)
  string_len = len(string_num)
  
  even_sum = 0
  odd_sum = 0
  
  for index in range(string_len):
    
    int_digit = int(string_num[index])
    
    if index % 2 == 0:
      even_sum += int_digit
    else:
      odd_sum += int_digit
  
  if odd_sum == even_sum:
    print(num, end=" ")
