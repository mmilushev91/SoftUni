player_1 = input()
player_2 = input()

player_1_points, player_2_points = 0, 0

command = input()

while command != "End of game":
    player_1_card = int(command)
    player_2_card = int(input())

    if player_1_card > player_2_card:
        player_1_points += player_1_card - player_2_card
    elif player_2_card > player_1_card:
        player_2_points += player_2_card - player_1_card
    else:
        print("Number wars!")

        player_1_card = int(input())
        player_2_card = int(input())

        winner = None
        winner_points = 0

        if player_1_card > player_2_card:
            winner = player_1
            winner_points = player_1_points
        elif player_2_card > player_1_card:
            winner = player_2
            winner_points = player_2_points

        print(f"{winner} is winner with {winner_points} points")

        break

    command = input()

else:
    print(f"{player_1} has {player_1_points} points")
    print(f"{player_2} has {player_2_points} points")
