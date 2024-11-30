ticket_prices = {
    "Quarter final": {
        "Standard": 55.50,
        "Premium": 105.20,
        "VIP": 118.90,
    },

    "Semi final": {
        "Standard": 75.88,
        "Premium": 125.22,
        "VIP": 300.40,
    },

    "Final": {
        "Standard": 110.10,
        "Premium": 160.66,
        "VIP": 400,
    }
}

stage = input()
ticket_type = input()
ticket_count = int(input())
trophy_picture = input()

trophy_picture_price = 0

if trophy_picture == "Y":
    trophy_picture_price = ticket_count * 40

total_price = ticket_count * ticket_prices[stage][ticket_type]

if total_price > 4000:
    trophy_picture_price = 0
    total_price -= total_price * 0.25

elif total_price > 2500:
    total_price -= total_price * 0.10

final_price = total_price + trophy_picture_price

print(f"{final_price:.2f}")
