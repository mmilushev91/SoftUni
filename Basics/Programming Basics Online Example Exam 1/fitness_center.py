training_types = {
    "Back": 0,
    "Chest": 0,
    "Legs": 0,
    "Abs": 0,
}

protein_buyers = {
    "Protein shake": 0,
    "Protein bar": 0,
}

visitors = int(input())

protein_buyers_count, training_types_count = 0, 0

for _ in range(visitors):

    activity = input()

    if activity in protein_buyers:
        protein_buyers[activity] += 1
        protein_buyers_count += 1
    else:
        training_types[activity] += 1
        training_types_count += 1

print(f"{training_types['Back']} - back")
print(f"{training_types['Chest']} - chest")
print(f"{training_types['Legs']} - legs")
print(f"{training_types['Abs']} - abs")
print(f"{protein_buyers['Protein shake']} - protein shake")
print(f"{protein_buyers['Protein bar']} - protein bar")
print(f"{training_types_count / visitors * 100:.2f}% - work out")
print(f"{protein_buyers_count / visitors * 100:.2f}% - protein")
