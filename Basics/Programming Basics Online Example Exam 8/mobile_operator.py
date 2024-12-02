mobile_plans = {
    "one": {
        "Small": 9.98,
        "Middle": 18.99,
        "Large": 25.98,
        "ExtraLarge": 35.99,
    },

    "two": {
        "Small": 8.58,
        "Middle": 17.09,
        "Large": 23.59,
        "ExtraLarge": 31.79,
    },
}

period = input()
mobile_plan = input()
added_internet = input()
bill_period = int(input())

bill = mobile_plans[period][mobile_plan]

if added_internet == "yes":
    if bill <= 10:
        bill += 5.50
    elif bill <= 30:
        bill += 4.35
    else:
        bill += 3.85

if period == "two":
    bill *= 0.9625

bill *= bill_period

print(f"{bill:.2f} lv.")
