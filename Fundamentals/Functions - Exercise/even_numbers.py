def return_even(num_list):
  even_list = list(filter(lambda x: x % 2 == 0, num_list))
  
  return even_list

number_list = [int(num) for num in input().split()]

print(return_even(number_list))
