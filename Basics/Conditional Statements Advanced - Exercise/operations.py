OPERATIONS = {
    "+": lambda x,y: x + y,
    "-": lambda x,y: x - y,
    "*": lambda x,y: x * y,
    "/": lambda x,y: x / y,
    "%": lambda x,y: x % y,
}

FIRST_OPERATIONS = ["+", "-", "*"]

num1 = int(input())
num2 = int(input())
operator = input()

if operator in FIRST_OPERATIONS:
    
    result = OPERATIONS[operator](num1, num2)
    resylt_type = "even" if result % 2 == 0 else "odd"
    
    print(f"{num1} {operator} {num2} = {result} - {resylt_type}")
    
else:
    
    if num2 == 0:
        print(f"Cannot divide {num1} by zero")
    else:
        result = OPERATIONS[operator](num1, num2)
        
        if operator == "/":
            result = f"{result:.2f}"
        
        print(f"{num1} {operator} {num2} = {result}")
