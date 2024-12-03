days_count = int(input())

earned_money = 0
total_games = 0
total_wins = 0

for _ in range(days_count):

    command = input()

    daily_games = 0
    daily_wins = 0
    daily_earned = 0

    while command != "Finish":
        sport = command
        result = input()

        daily_games += 1

        if result == "win":
            daily_wins += 1
            daily_earned += 20

        command = input()

    daily_loses = daily_games - daily_wins

    if daily_wins > daily_loses:
        daily_earned *= 1.10

    earned_money += daily_earned
    total_games += daily_games
    total_wins += daily_wins

total_loses = total_games - total_wins

if total_wins > total_loses:
    earned_money *= 1.20

    print(f"You won the tournament! Total raised money: {earned_money:.2f}")

else:
    print(f"You lost the tournament! Total raised money: {earned_money:.2f}")
