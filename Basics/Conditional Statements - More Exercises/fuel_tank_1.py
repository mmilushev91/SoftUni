RECHARGE_LIMIT = 25
VALID_FUELS = ["Diesel", "Gasoline", "Gas"]

fuel_type = input()
tank_litters = int(input())

if fuel_type not in VALID_FUELS:
  print("Invalid fuel!")
  quit()

lower_case = fuel_type[0].lower()
lower_case_fuel_type = f"{lower_case}{fuel_type[1::]}"

if tank_litters >= RECHARGE_LIMIT:
  print(f"You have enough {lower_case_fuel_type}.")
  
else:
  print(f"Fill your tank with {lower_case_fuel_type}!")
  
