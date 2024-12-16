numbered_tasks = [0] * 10

command = input()

while command != "End":
  index, task = command.split("-")
  
  numbered_tasks[int(index) - 1] = task
  
  command = input()

numbered_tasks = [item for item in numbered_tasks if item != 0]

print(numbered_tasks)
