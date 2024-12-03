free_space = float(input())

suitcases_count = 0
counter = 0

command = input()

while command != "End":

    suitcase_size = float(command)
    
    counter += 1
    
    if counter % 3 == 0:
        suitcase_size *= 1.10

    if suitcase_size > free_space:
        print("No more space!")
        break

    suitcases_count += 1

    free_space -= suitcase_size

    command = input()

else:
    print("Congratulations! All suitcases are loaded!")

print(f"Statistic: {suitcases_count} suitcases loaded.")
