lessons = input().split(", ")

command = input()

while command != "course start":
  command_line = command.split(":")
  
  action = command_line[0]
  lesson_title = command_line[1]
  
  lesson_exercise = f"{lesson_title}-Exercise"
  
  if action == "Add":
    
    if lesson_title not in lessons:
      lessons.append(lesson_title)
    
  elif action == "Insert":
    index = int(command_line[2])
    
    if lesson_title not in lessons:
      lessons.insert(index, lesson_title)
  
  elif action == "Remove":
    
    if lesson_title in lessons:
      lessons.remove(lesson_title)
    
    if lesson_exercise in lessons:
      lessons.remove(lesson_exercise)
      
  elif action == "Swap":
    swap_lesson = command_line[2]
    swap_lesson_exercise = f"{swap_lesson}-Exercise"
    
    if lesson_title in lessons and swap_lesson in lessons:
      lesson_title_index = lessons.index(lesson_title)
      swap_lesson_index = lessons.index(swap_lesson)
      
      lessons[lesson_title_index] = swap_lesson
      lessons[swap_lesson_index] = lesson_title
      
      if lesson_exercise in lessons:
        lessons.remove(lesson_exercise)
        lesson_title_new_index = lessons.index(lesson_title)
        lessons.insert(lesson_title_new_index + 1, lesson_exercise)
      
      if swap_lesson_exercise in lessons:
        lessons.remove(swap_lesson_exercise)
        swap_lesson_new_index = lessons.index(swap_lesson)
        lessons.insert(swap_lesson_new_index + 1, swap_lesson_exercise)
      
  elif action == "Exercise":
    if lesson_title in lessons:
      
      if lesson_exercise not in lessons:
        lesson_title_index = lessons.index(lesson_title)
        lessons.insert(lesson_title_index + 1, lesson_exercise)
    else:
      lessons.extend([lesson_title, lesson_exercise])

  command = input()

for i in range(len(lessons)):
  print(f"{i + 1}.{lessons[i]}")
