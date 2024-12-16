def solve(input_grade):
  
  if input_grade < 3:
    return "Fail"
  elif input_grade < 3.5:
    return "Poor"
  elif input_grade < 4.50:
    return "Good"
  elif input_grade < 5.50:
    return "Very Good"
  else:
    return "Excellent"

grade = float(input())

print(solve(grade))
