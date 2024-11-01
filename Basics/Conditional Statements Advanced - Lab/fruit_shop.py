WORK_DAYS_PRICES = {
    "banana":2.50,
    "apple": 1.20,
    "orange": 0.85,
    "grapefruit": 1.45,
    "kiwi": 2.70,
    "pineapple": 5.50,
    "grapes": 3.85,
}

WEEKEND_PRICES = {
    "banana":2.70,
    "apple": 1.25,
    "orange": 0.90,
    "grapefruit": 1.60,
    "kiwi": 3.00,
    "pineapple": 5.60,
    "grapes": 4.20,
}

WORK_DAYS_COUNT = 5

WEEK_DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday" ]
WORK_DAYS = WEEK_DAYS[:WORK_DAYS_COUNT]
WEEKEND_DAYS = WEEK_DAYS[WORK_DAYS_COUNT::]

fruit = input()
day = input()
quantity = float(input())

price = 0

if fruit not in WORK_DAYS_PRICES.keys() or day not in WEEK_DAYS:
    print("error")
    quit()
    
if day in WORK_DAYS:
    price = WORK_DAYS_PRICES[fruit] 
else:
    price = WEEKEND_PRICES[fruit]

bill = quantity * price

print(f"{bill:.2f}")
