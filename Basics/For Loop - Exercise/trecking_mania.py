groups_count = int(input())

musala, monblan, kilimandjaro, k2, everest = 0, 0, 0, 0, 0
total_climbers = 0

for _ in range(groups_count):
  group_count = int(input())
  
  if group_count <= 5:
    musala += group_count
  elif group_count <= 12:
    monblan += group_count
  elif group_count <= 25:
    kilimandjaro += group_count
  elif group_count <= 40:
    k2 += group_count
  else:
    everest += group_count
  
  total_climbers += group_count

print(f"{musala / total_climbers * 100:.2f}%")
print(f"{monblan / total_climbers * 100:.2f}%")
print(f"{kilimandjaro / total_climbers * 100:.2f}%")
print(f"{k2 / total_climbers * 100:.2f}%")
print(f"{everest / total_climbers * 100:.2f}%")
