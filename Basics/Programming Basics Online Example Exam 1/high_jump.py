height_to_beat = int(input())

train_height = height_to_beat - 30

jumps_counter = 0
fail_counter = 0

while height_to_beat >= train_height:

    attempt_height = int(input())

    jumps_counter += 1

    if attempt_height > train_height:
        fail_counter = 0
        train_height += 5
    else:
        fail_counter += 1

    if fail_counter == 3:
        print(f"Tihomir failed at {train_height}cm after {jumps_counter} jumps.")
        break

else:
    print(f"Tihomir succeeded, he jumped over {height_to_beat}cm after {jumps_counter} jumps.")
