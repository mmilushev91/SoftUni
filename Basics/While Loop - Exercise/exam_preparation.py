poor_grades_limit = int(input())
command = input()

task_counter = 0
poor_grades_counter = 0
sum_grades = 0
last_problem = None

while command != "Enough":
  task = command
  grade = int(input())
  
  task_counter += 1
  sum_grades += grade
  last_problem = task
  
  if grade <= 4:
    poor_grades_counter += 1 
    
    if poor_grades_counter == poor_grades_limit:
      print(f"You need a break, {poor_grades_counter} poor grades.")
      break
  command = input()
  
else:
  average_grade = sum_grades / task_counter
  
  print(f"Average score: {average_grade:.2f}")
  print(f"Number of problems: {task_counter}")
  print(f"Last problem: {last_problem}")
  
