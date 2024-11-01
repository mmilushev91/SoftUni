TOM_NORM = 30_000

YEAR_DAYS = 365

WORK_DAYS = 63
OFF_WORK_DAYS = 127

non_working_days = int(input())

work_days = YEAR_DAYS - non_working_days

work_days_playing_minutes = work_days * WORK_DAYS
non_working_days_playing_minutes = non_working_days * OFF_WORK_DAYS

total_playing_minutes = work_days_playing_minutes + non_working_days_playing_minutes

if total_playing_minutes > TOM_NORM:
  over_played_time = total_playing_minutes - TOM_NORM
  
  over_played_hours = over_played_time // 60
  over_played_minutes = over_played_time % 60
  
  print(f"Tom will run away")
  print(f"{over_played_hours} hours and {over_played_minutes} minutes more for play")

else:
  left_playing_time = TOM_NORM - total_playing_minutes
  left_playing_hours = left_playing_time // 60
  left_playing_minutes = left_playing_time % 60
  
  print("Tom sleeps well")
  print(f"{left_playing_hours} hours and {left_playing_minutes} minutes less for play")
  
