groups_count = int(input())

group1, group2, group3, group4, group5 = 0, 0, 0, 0, 0
total_climbers = 0

for _ in range(groups_count):

    group_count = int(input())

    if group_count <= 5:
        group1 += group_count

    elif group_count <= 12:
        group2 += group_count

    elif group_count <= 25:
        group3 += group_count

    elif group_count <= 40:
        group4 += group_count

    else:
        group5 += group_count

    total_climbers += group_count

print(f"{group1 / total_climbers * 100:.2f}%")
print(f"{group2 / total_climbers * 100:.2f}%")
print(f"{group3 / total_climbers * 100:.2f}%")
print(f"{group4 / total_climbers * 100:.2f}%")
print(f"{group5 / total_climbers * 100:.2f}%")
