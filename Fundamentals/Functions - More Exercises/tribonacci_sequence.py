def tribonacci_sequence(n):
  numbers = [1]

  for num in range(1, n):
    numbers.append(sum(numbers[-3:len(numbers)]))
  
  print(' '.join(str(num) for num in numbers))

n = int(input())

tribonacci_sequence(n)
