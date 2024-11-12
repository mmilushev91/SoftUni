interval = int(input()) * 2

sum_pair = 0
last_pair = 0
difference = 0

is_it_equal = True

for pos in range(1, interval + 1):
  number = int(input())
  
  sum_pair += number
  
  if pos % 2 == 0:
    if last_pair != 0 and last_pair != sum_pair:
      difference = abs(sum_pair - last_pair)
      is_it_equal = False
      
    last_pair = sum_pair
    sum_pair = 0

if is_it_equal:
  print(f"Yes, value={last_pair}")
else:
  print(f"No, maxdiff={difference}")
  
