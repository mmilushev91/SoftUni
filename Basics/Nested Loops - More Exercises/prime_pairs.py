def check_prime(number):

  for i in range(2, number):
    
    if number % i == 0:
      return False
  
  return True
  
start_first_pair = int(input())
start_second_pair = int(input())

end_first_pair = int(input()) + start_first_pair + 1
end_second_pair = int(input()) + start_second_pair + 1

for num1 in range(start_first_pair, end_first_pair):
  
  if not check_prime(num1):
    continue
    
  for num2 in range(start_second_pair, end_second_pair):
    
    if not check_prime(num2):
      continue
    
    print(f"{num1}{num2}")
