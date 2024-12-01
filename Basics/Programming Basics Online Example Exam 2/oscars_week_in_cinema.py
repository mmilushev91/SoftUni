ticket_prices = {
    "A Star Is Born": {
        "normal": 7.50,
        "luxury": 10.50,
        "ultra luxury": 13.50,
    },

    "Bohemian Rhapsody": {
        "normal": 7.35,
        "luxury": 9.45,
        "ultra luxury": 12.75,
    },

    "Green Book": {
        "normal": 8.15,
        "luxury": 10.25,
        "ultra luxury": 13.25,
    },

    "The Favourite": {
        "normal": 8.75,
        "luxury": 11.55,
        "ultra luxury": 13.95,
    },

}

movie_name = input()
hall_type = input()
ticket_count = int(input())

ticket_price = ticket_prices[movie_name][hall_type]
total_price = ticket_price * ticket_count

print(f"{movie_name} -> {total_price:.2f} lv.")
