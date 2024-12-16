def multiplication_sign(numbers):
  negative_count = 0
  
  for num in numbers:
    
    if num == 0:
      print("zero")
      break
    
    if num < 0:
      negative_count += 1 
  
  else:
    if negative_count == 0 or negative_count == 2:
      print("positive")
    else:
      print("negative")

nums = [int(input()), int(input()), int(input())]
    
multiplication_sign(nums)
