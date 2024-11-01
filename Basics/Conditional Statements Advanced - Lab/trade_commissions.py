CITIES_COMMISSIONS = {
    "Sofia": [0.05,	0.07, 0.08,	0.12],
    "Varna": [0.045,	0.075, 0.10, 0.13],
    "Plovdiv": [0.055, 0.08, 0.12,	0.145],
}

COMMISSION_LEVELS = [0, 500, 1000, 10_000]

city = input()
sales = float(input())

commission_percent = 0

if city not in CITIES_COMMISSIONS.keys() or sales < 0:
    print("error")
    quit()
    
if COMMISSION_LEVELS[0] <= sales <= COMMISSION_LEVELS[1]:
    commission_percent = CITIES_COMMISSIONS[city][0]
elif sales <= COMMISSION_LEVELS[2]:
    commission_percent = CITIES_COMMISSIONS[city][1]
elif sales <= COMMISSION_LEVELS[3]:
    commission_percent = CITIES_COMMISSIONS[city][2]
else:
    commission_percent = CITIES_COMMISSIONS[city][3]

commission = sales * commission_percent

print(f"{commission:.2f}")
