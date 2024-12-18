strings = input().split()

command = input()

while command !="3:1":
  command_line = command.split()
  
  action = command_line[0]

  if action == "merge":
    start_index = int(command_line[1])
    end_index = int(command_line[2])
    
    if start_index < 0:
      start_index = 0
    
    if end_index >= len(strings):
      end_index = len(strings) - 1
    
    merged_string = "".join(strings[start_index:end_index + 1])
    
    for _ in range(start_index, end_index + 1):
      strings.pop(start_index)
    
    strings.insert(start_index, merged_string)
    
  elif action == "divide":
    index = int(command_line[1])
    parts = int(command_line[2])
    
    divided_string = strings.pop(index)
    substring_len = len(divided_string) // parts
    last_item_len = substring_len + (len(divided_string) % parts)
    for_loop_range = len(divided_string) - last_item_len
    
    substring = ""
    substrings = []
      
    for i in range(for_loop_range):
        
      substring += divided_string[i]
        
      if len(substring) == substring_len:
        substrings.append(substring)
        substring = ""
      
    substrings.append(divided_string[-last_item_len::])
    
    for i in range(len(substrings)):
      strings.insert(index + i, substrings[i])
  
  command = input()

print(' '.join(strings))
