herd = input().split(", ")

herd. reverse()

herd_len = len(herd)

for index in range(herd_len - 1, -1, -1):

    if index == 0 and herd[index] == "wolf":
        print("Please go away and stop eating my sheep")
        break

    if herd[index] == "wolf":
        print(f"Oi! Sheep number {index}! You are about to be eaten by a wolf!")
        break
