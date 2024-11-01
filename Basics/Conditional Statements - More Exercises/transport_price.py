BUS_MIN_DISTANCE = 20
BUS_TAX_KM = 0.09

TRAIN_MIN_DISTANCE = 100
TRAIN_TAX_KM = 0.06

TAXI_START_TAX_KM = 0.70
TAXI_DAILY_TAX_KM = 0.79
TAXI_NIGHT_TAX_KM = 0.90

travel_deistance_km = int(input())
time = input()

tax = 0
taxi_start_tax = 0

if travel_deistance_km >= TRAIN_MIN_DISTANCE:
  tax = TRAIN_TAX_KM
elif travel_deistance_km >= BUS_MIN_DISTANCE:
  tax = BUS_TAX_KM
  
else:
  taxi_start_tax = TAXI_START_TAX_KM
  
  if time == "day":
    tax = TAXI_DAILY_TAX_KM

  elif time == "night":
    tax = TAXI_NIGHT_TAX_KM

travel_cost = travel_deistance_km * tax + taxi_start_tax

print(f"{travel_cost:.2f}")
