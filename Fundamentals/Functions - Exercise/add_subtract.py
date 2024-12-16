def add_and_subtract(num1, num2, num3):
  def sum_numbers():
    return num1 + num2
  
  def subtract():
    return sum_numbers() - num3
  
  return subtract() 

number1 = int(input())
number2 = int(input())
number3 = int(input())

print(add_and_subtract(number1, number2, number3))
