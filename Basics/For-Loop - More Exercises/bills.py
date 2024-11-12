period = int(input())

water = period * 20
internet = period * 15

electricity = sum(float(input()) for _ in range(period))

sum_no_other_bills = water + internet + electricity

others = sum_no_other_bills + sum_no_other_bills * 0.20

total_bills = sum_no_other_bills + others

average = total_bills / period

print(f"Electricity: {electricity:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {others:.2f} lv")
print(f"Average: {average:.2f} lv")
