def calculations(num1, num2, operation):
  operations = {
    "multiply": lambda x,y: x * y,
    "divide":  lambda x,y: x / y,
    "add":  lambda x,y: x + y,
    "subtract":  lambda x,y: x - y,
  }
  
  result = operations[operation](num1, num2)
  
  return int(result)

input_operation = input()

number1 = int(input())
number2 = int(input())

print(calculations(number1, number2, input_operation))
