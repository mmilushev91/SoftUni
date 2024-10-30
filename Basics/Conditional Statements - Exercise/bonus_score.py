BONUS_TO_THOUSAND = 0.20
BONUS_ABOVE_THOUSAND = 0.10

start_points = int(input())

bonus_points = 0

if start_points <= 100:
  bonus_points += 5
elif start_points <= 1000:
  bonus_points += start_points * BONUS_TO_THOUSAND
else:
  bonus_points += start_points * BONUS_ABOVE_THOUSAND

if start_points % 2 == 0:
  bonus_points += 1
elif start_points % 10 == 5:
  bonus_points += 2

final_points = start_points + bonus_points

print(bonus_points)
print(final_points)
