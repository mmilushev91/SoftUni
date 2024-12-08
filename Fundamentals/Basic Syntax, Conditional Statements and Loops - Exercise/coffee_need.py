command = input()

events = ["coding", "dog", "cat", "movie"]
coffees_count = 0

while command != "END":
    event = command

    if event.lower() in events:
        if event.islower():
            coffees_count += 1
        else:
            coffees_count += 2
    if coffees_count >= 5:
        print("You need extra sleep")
        break

    command = input()
else:
    print(coffees_count)
