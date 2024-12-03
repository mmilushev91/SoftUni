walk_minutes = int(input())
daily_walks_count = int(input())
daily_calories_intake = int(input())

total_walk_minutes = walk_minutes * daily_walks_count
spend_calories = total_walk_minutes * 5
left_calories = daily_calories_intake - spend_calories

max_left_calories = daily_calories_intake * 0.50

if left_calories <= max_left_calories:
  print(f"Yes, the walk for your cat is enough. Burned calories per day: {spend_calories}." )
else:
  print(f"No, the walk for your cat is not enough. Burned calories per day: {spend_calories}.")
