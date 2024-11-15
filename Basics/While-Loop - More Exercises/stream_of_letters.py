COMMAND_CHARS = ["c", "o", "n"]

command_chars = COMMAND_CHARS.copy()

word = ""

while True:
  
  command = input()
  
  if command == "End":
    break 
  
  char = command
  
  if not char.isalpha():
    continue
  
  if char in command_chars:
    command_chars.remove(char)
  
    if not command_chars:
      
      command_chars.extend(COMMAND_CHARS.copy())
      
      print(word, end=" ")
      
      word = ""
      
    continue
  
  
  word += char
