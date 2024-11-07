HOTEL_PRICES = {
    "room for one person": [18.00],
    "apartment": [25.00, 0.30, 0.35, 0.50],
    "president apartment": [35.00, 0.10, 0.15, 0.20],
}

DISCOUNT_DAYS = [10, 15]

GRADE_PERCENT = [0.10, 0.25]
GRADE_TYPE = ["negative", "positive"]

NO_DISCOUNT_ROOM = "room for one person"
DAY_SUBTRACTER = 1

days = int(input())
room_type = input()
grade = input()

nights = days - DAY_SUBTRACTER
room_price = HOTEL_PRICES[room_type][0]

if room_type != NO_DISCOUNT_ROOM:
    
    if nights < DISCOUNT_DAYS[0]:
        room_price -= room_price * HOTEL_PRICES[room_type][1]
    elif nights <= DISCOUNT_DAYS[1]:
        room_price -= room_price * HOTEL_PRICES[room_type][2]
    else:
        room_price -= room_price * HOTEL_PRICES[room_type][3]

if grade == GRADE_TYPE[0]:
    room_price -= room_price * GRADE_PERCENT[0]
elif grade == GRADE_TYPE[1]:
    room_price += room_price * GRADE_PERCENT[1]

final_price = room_price * nights

print(f"{final_price:.2f}")
