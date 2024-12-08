decoration_count = int(input())
days = int(input())

decorations_info = {
    "Ornament Set": [2, 5],
    "Tree Skirt": [5, 3],
    "Tree Garland": [3, 10],
    "Tree Lights": [15, 17],
}

total_spirit = 0
total_cost = 0

for day in range(1, days + 1):

    if day % 11 == 0:
        decoration_count += 2

    if day % 2 == 0:
        total_cost += decoration_count * (decorations_info["Ornament Set"][0])
        total_spirit += decorations_info["Ornament Set"][1]

    if day % 3 == 0:
        total_cost += decoration_count * (decorations_info["Tree Skirt"][0] + decorations_info["Tree Garland"][0])
        total_spirit += decorations_info["Tree Skirt"][1] + decorations_info["Tree Garland"][1]

    if day % 5 == 0:
        total_cost += decoration_count * (decorations_info["Tree Lights"][0])
        total_spirit += decorations_info["Tree Lights"][1]

        if day % 3 == 0:
            total_spirit += 30

    if day % 10 == 0:
        total_spirit -= 20

        total_cost += decorations_info["Tree Skirt"][0] + decorations_info["Tree Garland"][0]\
                     + decorations_info["Tree Lights"][0]

        if day == days:
            total_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")
