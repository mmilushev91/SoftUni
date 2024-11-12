numbers_count = int(input())

float_inf = float("inf")
float_minus_inf = float("-inf")

odd_sum = 0
odd_min = float_inf
odd_max = float_minus_inf

even_sum = 0
even_min = float_inf
even_max = float_minus_inf

for pos in range(1, numbers_count + 1):
  num = float(input())
  
  if pos % 2 != 0:
    odd_sum += num 
    
    if num < odd_min:
      odd_min = num
    
    if num > odd_max:
      odd_max = num
  
  else:
    
    even_sum += num
    
    if num < even_min:
      even_min = num
    
    if num > even_max:
      even_max = num

print(f"OddSum={odd_sum:.2f},")
print(f"OddMin={odd_min:.2f}," if odd_min != float_inf else "OddMin=No,")
print(f"OddMax={odd_max:.2f}," if odd_max != float_minus_inf else "OddMax=No,")

print(f"EvenSum={even_sum:.2f},")
print(f"EvenMin={even_min:.2f}," if even_min != float_inf else "EvenMin=No,")
print(f"EvenMax={even_max:.2f}" if even_max != float_minus_inf else "EvenMax=No")
