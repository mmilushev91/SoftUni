student_count = int(input())

first_group, second_group, third_group, fourth_group = 0, 0, 0, 0
grades_sum = 0

for _ in range(student_count):
  grade = float(input())
  
  grades_sum += grade
  
  if grade < 3:
    first_group += 1 
  
  elif grade < 4:
    second_group += 1
  
  elif grade < 5:
    third_group += 1 
    
  else:
    fourth_group += 1

average_grade = grades_sum / student_count
  
print(f"Top students: {fourth_group / student_count * 100:.2f}%")
print(f"Between 4.00 and 4.99: {third_group / student_count * 100:.2f}%")
print(f"Between 3.00 and 3.99: {second_group / student_count * 100:.2f}%")
print(f"Fail: {first_group / student_count * 100:.2f}%")
print(f"Average: {average_grade:.2f}")
    
