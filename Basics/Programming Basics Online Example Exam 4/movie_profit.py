movie_name = input()
days = int(input())
ticket_count = int(input())
ticket_price = float(input())
cinema_tax_percent = int(input()) / 100

income = days * (ticket_count * ticket_price)
cinema_tax = income * cinema_tax_percent
net_income = income - cinema_tax

print(f"The profit from the movie {movie_name} is {net_income:.2f} lv.")
