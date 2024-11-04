FIND_DESTINATION = {
    100: {
        "Bulgaria": {
            "summer": 0.30,
            "winter": 0.70
        }
    },
    
    1000: {
        "Balkans": {
            "summer": 0.40,
            "winter": 0.80
        }
    }
}

EUROPE_DESTINATION = "Europe"
EUROPE_BUDGET_PERCENT = 0.90

REST_TYPES = ["Camp", "Hotel"]
START_SEASON = "summer"


budget = float(input())
season = input()

destination = None
rest_type = REST_TYPES[1]
budget_percent = 0


for item in FIND_DESTINATION:
    
    if budget <= item:
        for key in FIND_DESTINATION[item]:
            destination = key
            budget_percent = FIND_DESTINATION[item][destination][season]
            
            if season == START_SEASON:
                rest_type = REST_TYPES[0]
            break
        break
    
else:
    destination = EUROPE_DESTINATION
    budget_percent = EUROPE_BUDGET_PERCENT
    
spent_money = budget * budget_percent

print(f"Somewhere in {destination}")
print(f"{rest_type} - {spent_money:.2f}")
