def find_factorial(num):
  
  factorial = 1
  
  for i in range(1, num + 1):
      factorial *= i
  
  return factorial

num1 = int(input())
num2 = int(input())

result = find_factorial(num1) / find_factorial(num2)

print(f"{result:.2f}")
