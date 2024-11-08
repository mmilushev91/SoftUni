SPORT_PRICES = {
    "Winter": {
        "girls": [9.60, "Gymnastics"],
        "boys": [9.60, "Judo"],
        "mixed": [10, "Ski"],
    },
    
    "Spring": {
        "girls": [7.20, "Athletics"],
        "boys": [7.20, "Tennis"],
        "mixed": [9.50, "Cycling"],
    },
    
    "Summer": {
        "girls": [15, "Cycling"],
        "boys": [15, "Football"],
        "mixed": [20, "Swimming"],
    },
}

season = input()
group_type = input()

student_count = int(input())
nights_count = int(input())

single_price = SPORT_PRICES[season][group_type][0]
sport_name = SPORT_PRICES[season][group_type][1]

if 10 <= student_count < 20:
    single_price -= single_price * 0.05
elif 20 <= student_count < 50:
    single_price -= single_price * 0.15
elif student_count >= 50:
    single_price -= single_price * 0.50

final_price = (single_price * student_count) * nights_count

print(f"{sport_name} {final_price:.2f} lv.")
