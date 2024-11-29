LETTER_START = 97

n = int(input()) + 1
l = int(input()) + LETTER_START

for num1 in range(1, n):
  for num2 in range(1, n):
    for letter1 in range(LETTER_START, l):
      for letter2 in range(LETTER_START, l):
        for num3 in range(1, n):
          
          if num3 <= num1 or num3 <= num2:
            continue
          
          print(f"{num1}{num2}{chr(letter1)}{chr(letter2)}{num3}", end=" ")
