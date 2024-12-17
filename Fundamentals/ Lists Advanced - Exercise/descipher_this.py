message = input().split()

for word in message:
  end_index = 0
  
  for char in word:
    if not char.isdigit():
      end_index = word.index(char)
      break
  
  list_word = list(word)
  replace_char = chr(int(''.join(list_word[:end_index])))
    
  list_word[:end_index] = replace_char
    
  second_char = list_word[1]
  list_word[1] = list_word[-1]
  list_word[-1] = second_char
    
  print("".join(list_word), end=" ")
