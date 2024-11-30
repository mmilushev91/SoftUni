stage_points = {
    "W": 2000,
    "F": 1200,
    "SF": 720,
}

tournaments_count = int(input())
start_points = int(input())

points = 0
wins = 0

for _ in range(tournaments_count):

    stage = input()

    points += stage_points[stage]

    if stage == "W":
        wins += 1

final_points = points + start_points
average_points = int(points / tournaments_count)
wins_percent = wins / tournaments_count * 100

print(f"Final points: {final_points}")
print(f"Average points: {average_points}")
print(f"{wins_percent:.2f}%")
