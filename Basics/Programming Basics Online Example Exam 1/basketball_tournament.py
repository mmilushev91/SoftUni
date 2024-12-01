command = input()

total_matches = 0
wins = 0
loses = 0

while command != "End of tournaments":
    tournament_name = command

    matches = int(input())

    total_matches += matches

    for num in range(1, matches + 1):
        jessie_team_score = int(input())
        opposing_team_score = int(input())

        difference = abs(jessie_team_score - opposing_team_score)

        if jessie_team_score > opposing_team_score:
            wins += 1

            print(f"Game {num} of tournament {tournament_name}: win with {difference} points.")
        else:
            loses += 1

            print(f"Game {num} of tournament {tournament_name}: lost with {difference} points.")

    command = input()

print(f"{wins / total_matches * 100:.2f}% matches win")
print(f"{loses / total_matches * 100:.2f}% matches lost")
