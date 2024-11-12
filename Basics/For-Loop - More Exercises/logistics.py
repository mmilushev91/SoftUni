cargo_count = int(input())

microbus_cargo, truck_cargo, train_cargo = 0, 0, 0

for _ in range(cargo_count):
  cargo = int(input())
  
  if cargo <= 3:
    microbus_cargo += cargo
  elif cargo <= 11:
    truck_cargo += cargo
  else:
    train_cargo += cargo

total_cargo = microbus_cargo + train_cargo + truck_cargo
average_price = ((microbus_cargo * 200) + (truck_cargo * 175) + (train_cargo * 120)) / total_cargo

print(f"{average_price:.2f}")
print(f"{microbus_cargo / total_cargo * 100:.2f}%")
print(f"{truck_cargo / total_cargo * 100:.2f}%")
print(f"{train_cargo / total_cargo * 100:.2f}%")
