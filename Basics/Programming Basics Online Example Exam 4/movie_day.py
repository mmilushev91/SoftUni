action_time = int(input())
sceenes_count = int(input())
sceene_time = int(input())

prep_time = action_time * 0.15
sceenes_time = sceenes_count * sceene_time
total_time = sceenes_time + prep_time

if action_time >= total_time:
  left_time = action_time - total_time
  
  print(f"You managed to finish the movie on time! You have {round(left_time)} minutes left!")

else:
  time_needed = total_time - action_time
  
  print(f"Time is up! To complete the movie you need {round(time_needed)} minutes.")
