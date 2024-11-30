multipliers = {
    "Triple": 3,
    "Double": 2,
    "Single": 1,
}

points = 301

name = input()

successful_shots, unsuccessful_shots = 0, 0

while points > 0:

    command = input()

    if command == "Retire":
        print(f"{name} retired after {unsuccessful_shots} unsuccessful shots.")
        break

    multiplier = command

    current_points = int(input())

    subtract_points = multipliers[multiplier] * current_points

    if subtract_points > points:
        unsuccessful_shots += 1
        continue

    successful_shots += 1
    points -= subtract_points

else:
    print(f"{name} won the leg with {successful_shots} shots.")
