number = int(input())

if number <= 1:
  print(False)

else:
  for num in range(2, number):
    
    if number % num == 0:
      print(False)
      break
  
  else:
    print(True)
