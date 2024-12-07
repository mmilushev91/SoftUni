number = float(input())

result = ""

if 0 < abs(number) < 1:
    result += "small "
elif abs(number) > 1_000_000:
    result += "large "

if number == 0:
    result = "zero"
elif number < 0:
    result += "negative"
else:
    result += "positive"

print(result)
