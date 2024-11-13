SCHOOL_YEARS = 12

student_name = input()

sum_grades = 0
poor_grades = 0
year = 0

while year < SCHOOL_YEARS:
  grade = float(input())
  if grade < 4:
    poor_grades += 1 
    
    if poor_grades == 2:
      year += 1
      print(f"{student_name} has been excluded at {year} grade")
      break
  else:
    sum_grades += grade
    year += 1
    
else:
  average_grade = sum_grades / SCHOOL_YEARS
  print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
