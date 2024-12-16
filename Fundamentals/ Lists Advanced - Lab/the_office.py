numbers = [int(num) for num in input().split()]
factor = int(input())

total_people_count = len(numbers)
multiplied_by_factor = [num * factor for num in numbers]
average_happiness = sum(multiplied_by_factor) / total_people_count
half_people_count = total_people_count / 2

happy_count = len([num for num in multiplied_by_factor if num >= average_happiness])

if happy_count >= half_people_count:
  print(f"Score: {happy_count}/{total_people_count}. Employees are happy!")
else:
  print(f"Score: {happy_count}/{total_people_count}. Employees are not happy!")
