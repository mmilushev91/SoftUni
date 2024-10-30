deposit = float(input())
period = int(input())
montly_interest_rate = (float(input()) / 100) / 12

calculated_grow = (deposit * montly_interest_rate) * period

total_money = calculated_grow + deposit

print(total_money)
