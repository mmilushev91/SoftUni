packages_prices = {
    "John Wick": {
        "Drink": 12,
        "Popcorn": 15,
        "Menu": 19,
    },

    "Star Wars": {
        "Drink": 18,
        "Popcorn": 25,
        "Menu": 30,
    },

    "Jumanji": {
        "Drink": 9,
        "Popcorn": 11,
        "Menu": 14,
    },
}

movie = input()
package_type = input()
ticket_count = int(input())

total_price = ticket_count * packages_prices[movie][package_type]

if movie == "Star Wars" and ticket_count >= 4:
    total_price *= 0.70

if movie == "Jumanji" and ticket_count == 2:
    total_price *= 0.85

print(f"Your bill is {total_price:.2f} leva.")
