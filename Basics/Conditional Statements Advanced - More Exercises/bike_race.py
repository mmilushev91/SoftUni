JUNNIORS = "juniors"
SENIOURS = "seniors"

TAXES = {
    "juniors": {
        "trail": 5.50,
        "cross-country": 8,
        "downhill": 12.25,
        "road": 20,
    },
    
    "seniors": {
        "trail": 7,
        "cross-country": 9.50,
        "downhill": 13.75,
        "road": 21.50,
    }
}

PERCENTS = [0.05, 0.25]
DISCOUNT_COUNT = 50
DISCOUNT_TRACE = "cross-country"

juniours_count = int(input())
seniours_count = int(input())
trace_type = input()

juniour_tax = TAXES[JUNNIORS][trace_type]
seniour_tax = TAXES[SENIOURS][trace_type]

if juniours_count + seniours_count >= DISCOUNT_COUNT and trace_type == DISCOUNT_TRACE:
    juniour_tax -= juniour_tax * PERCENTS[1]
    seniour_tax -= seniour_tax * PERCENTS[1]

earned_money = juniours_count * juniour_tax + seniours_count * seniour_tax
tax = earned_money * PERCENTS[0]

earned_money -= tax

print(f"{earned_money:.2f}" )
