PUZZLE = 2.60
DOLL = 3
TEDDY_BEAR = 4.10
MINION = 8.20
TRUCK = 2

DISCOUNT = 0.25
RENT = 0.10

tour_cost = float(input())
puzzle_count = int(input())
doll_count = int(input())
teddy_bear_count = int(input())
minion_count = int(input())
truck_count = int(input())

income = (puzzle_count * PUZZLE) + (doll_count * DOLL) + (teddy_bear_count * TEDDY_BEAR) + (minion_count * MINION) + (truck_count * TRUCK)

toys_count = puzzle_count + doll_count + teddy_bear_count + minion_count + truck_count

if toys_count >= 50:
  income -= income * DISCOUNT

rent = income * RENT

income -= rent

if income >= tour_cost:
  money_left = income - tour_cost
  print(f"Yes! {money_left:.2f} lv left.")
else:
  money_needed = tour_cost - income
  print(f"Not enough money! {money_needed:.2f} lv needed.")
  
