fires = input().split("#")
water = int(input())

valid_ranges = {
  "High": range(81, 126),
  "Medium": range(51, 81),
  "Low": range(1, 51),
}
counter = 0
effort = 0
total_fire = 0

print("Cells: ")

while water > 0 and counter < len(fires):
  
  fire_type, value = fires[counter].split(" = ")
  
  value = int(value)
  
  if value in valid_ranges[fire_type]:
    if value <= water:
      water -= value
      effort += value * 0.25
      total_fire += value
  
      print(f" - {value}")
      
  counter += 1
  
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
