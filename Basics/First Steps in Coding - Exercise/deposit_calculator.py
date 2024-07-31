# Pseudocode

# prompt user for deposit amount(float), deposit interval(int), annual interest rate(float)
# calculate final sum: сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)
# print result

deposit_amount = float(input())
deposit_interval = int(input())
annual_interest_rate = float(input()) / 100

final_sum = deposit_amount + deposit_interval * \
((deposit_amount * annual_interest_rate) / 12)

print(final_sum)
