TICKET_PRICES = {
    "Premiere": 12.00,
    "Normal": 7.50,
    "Discount": 5.00,
}

screening_type = input()
cinema_rows = int(input())
cinema_columns = int(input())

total_places = cinema_rows * cinema_columns
ticket_price = TICKET_PRICES[screening_type]

income = total_places * ticket_price

print(f"{income:.2f} leva")
