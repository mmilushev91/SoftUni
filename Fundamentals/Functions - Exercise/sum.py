def sum_odd_even(num):
  even_sum = 0
  odd_sum = 0
  
  for digit in num:
    int_digit = int(digit)
    
    if int_digit % 2 == 0:
      even_sum += int_digit
    else:
      odd_sum += int_digit
  
  return [odd_sum, even_sum]

number = input()

result = sum_odd_even(number)

print(f"Odd sum = {result[0]}, Even sum = {result[1]}")
