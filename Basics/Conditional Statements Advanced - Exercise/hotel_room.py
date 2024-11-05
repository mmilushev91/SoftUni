test_dic = {
   "May": [50, 65],
   "October": [50, 65],
   "June": [75.20, 68.70],
   "September": [75.20, 68.70],
   "July": [76, 77],
   "August": [76, 77]
}

DISCOUNT_NIGHTS_COUNT = [7, 14]
DISCOUNT_MONTHS = ["May", "October", "June","September"]
DISCOUNT_PERCENTS = [0.05, 0.10, 0.20, 0.30]

month = input()
nights_count = int(input())

studio_price = test_dic[month][0] * nights_count
apartment_price = test_dic[month][1] * nights_count

if month == DISCOUNT_MONTHS[0] or month == DISCOUNT_MONTHS[1]:
    if nights_count > DISCOUNT_NIGHTS_COUNT[1]:
        studio_price -= studio_price * DISCOUNT_PERCENTS[3]
    elif nights_count > DISCOUNT_NIGHTS_COUNT[0]:
        studio_price -= studio_price * DISCOUNT_PERCENTS[0]

elif (month == DISCOUNT_MONTHS[2] or month == DISCOUNT_MONTHS[3])\
    and nights_count > DISCOUNT_NIGHTS_COUNT[1]:
        studio_price -= studio_price * DISCOUNT_PERCENTS[2]

if nights_count > DISCOUNT_NIGHTS_COUNT[1]:
    apartment_price -= apartment_price * DISCOUNT_PERCENTS[1]

print(f"Apartment: {apartment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")
