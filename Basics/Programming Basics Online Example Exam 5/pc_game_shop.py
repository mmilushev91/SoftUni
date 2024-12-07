sold_games = {
  "Hearthstone": 0,
  "Fornite": 0,
  "Overwatch": 0,
}

sold_games_count = int(input())

others = 0

for _ in range(sold_games_count):
  game = input()
  
  if game in sold_games:
    sold_games[game] += 1 
  else:
    others += 1 

print(f"Hearthstone - {sold_games['Hearthstone'] / sold_games_count * 100:.2f}%")
print(f"Fornite - {sold_games['Fornite'] / sold_games_count * 100:.2f}%")
print(f"Overwatch - {sold_games['Overwatch'] / sold_games_count * 100:.2f}%")
print(f"Others - {others / sold_games_count * 100:.2f}%")
