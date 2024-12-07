points = {
  "W": 3,
  "D": 1,
  "L": 0,
}

statistic = {
  "W": 0,
  "D": 0,
  "L": 0,
}

team_name = input()
matches_played = int(input())

if matches_played <= 0:
  print(f"{team_name} hasn't played any games during this season.")
  quit()

points_won = 0

for _ in range(matches_played):
  result = input()
  
  points_won += points[result]
  statistic[result] += 1

print(f"{team_name} has won {points_won} points during this season.")
print("Total stats:")
print(f"## W: {statistic['W']}")
print(f"## D: {statistic['D']}")
print(f"## L: {statistic['L']}")
print(f"Win rate: {statistic['W'] / matches_played * 100:.2f}%")
