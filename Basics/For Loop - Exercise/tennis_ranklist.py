POINTS_AMOUNT = {
  "W": 2000,
  "F": 1200,
  "SF": 720,
}

tournaments_count = int(input())
start_points = int(input())

points = 0
wins = 0

for _ in range(tournaments_count):
  tournament_round = input()
  
  points += POINTS_AMOUNT[tournament_round]
  
  if tournament_round == "W":
    wins += 1

final_points = points + start_points
average_points = points/ tournaments_count
wins_percent = wins / tournaments_count * 100

print(f"Final points: {final_points}")
print(f"Average points: {int(average_points)}")
print(f"{wins_percent:.2f}%")
