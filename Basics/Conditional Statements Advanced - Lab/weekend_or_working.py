DAYS = {
    "Monday": "Working day",
    "Tuesday": "Working day",
    "Wednesday": "Working day",
    "Thursday": "Working day",
    "Friday": "Working day",
    "Saturday": "Weekend",
    "Sunday": "Weekend",
}

day = input()

if day not in DAYS.keys():
    print("Error")
    quit()

print(DAYS[day])
