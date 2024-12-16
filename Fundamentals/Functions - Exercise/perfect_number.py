def find_perfect(number):
  
  sum_divisors = 0
  
  for divisor in range(1, number):
    
    if number % divisor == 0:
      sum_divisors += divisor
    
  if number == sum_divisors:
    print("We have a perfect number!")
  else:
    print("It's not so perfect." )
    
num = int(input())

find_perfect(num)
