tickets_count = {
    "student": 0,
    "standard": 0,
    "kid": 0,
}

command = input()

total_tickets = 0

while command != "Finish":
    movie_name = command

    free_spots = int(input())

    sold_tickets = 0

    while True:
        if sold_tickets == free_spots:
            break

        inner_command = input()

        if inner_command == "End":
            break

        ticket_type = inner_command

        tickets_count[ticket_type] += 1
        sold_tickets += 1

    print(f"{movie_name} - {sold_tickets / free_spots * 100:.2f}% full.")

    total_tickets += sold_tickets

    command = input()

print(f"Total tickets: {total_tickets}")
print(f"{tickets_count['student'] / total_tickets * 100:.2f}% student tickets.")
print(f"{tickets_count['standard'] / total_tickets * 100:.2f}% standard tickets.")
print(f"{tickets_count['kid'] / total_tickets * 100:.2f}% kids tickets.")
