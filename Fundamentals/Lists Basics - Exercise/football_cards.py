cards = input().split()

a_team = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
b_team = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

game_terminated = False

for card in cards:
    team, player = card.split("-")
    player = int(player)

    if team == "A":

        if player in a_team:
            a_team.remove(player)

    elif team == "B":
        if player in b_team:
            b_team.remove(player)

    if len(a_team) < 7 or len(b_team) < 7:
        game_terminated = True
        break

print(f"Team A - {len(a_team)}; Team B - {len(b_team)}")

if game_terminated:
    print("Game was terminated")
