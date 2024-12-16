kill_list = [num for num in input().split()]
kill_step = int(input()) - 1 

kill_index = 0
killed_list = []

while len(kill_list) > 0:
  kill_index += kill_step

  while kill_index >= len(kill_list):
    kill_index -= len(kill_list)
  
  killed_list.append(kill_list.pop(kill_index))
  
print(f"[{','.join(killed_list)}]")
