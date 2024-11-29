games = [input(), input(), input()]

wins, draws, loses = 0, 0, 0

for game in games:
    score_1, score_2 = [int(num) for num in game.split(":")]

    if score_1 > score_2:
        wins += 1
    elif score_1 == score_2:
        draws += 1
    else:
        loses += 1

print(f"Team won {wins} games.")
print(f"Team lost {loses} games.")
print(f"Drawn games: {draws}")
