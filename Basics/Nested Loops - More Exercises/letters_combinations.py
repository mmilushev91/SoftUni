start = ord(input())
end = ord(input())

letter_to_skip = input()

combinations = 0

for char1 in range(start, end + 1):
  for char2 in range(start, end + 1):
    for char3 in range(start, end + 1):
      letter1 = chr(char1)
      letter2 = chr(char2)
      letter3 = chr(char3)
      
      if letter1 == letter_to_skip \
        or letter2 == letter_to_skip \
        or letter3 == letter_to_skip:
      
        continue
      
      combinations += 1 
      
      print(f"{letter1}{letter2}{letter3}", end=" ")
  
print(combinations, end=" ")
