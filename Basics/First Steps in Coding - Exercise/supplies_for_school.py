PEN_PACKAGE_PRICE = 5.80
MARKER_PACKAGE_PRICE = 7.20
DETERGENT_PRICE = 1.20

pen_packages = int(input())
marker_packages = int(input())
detergent_liters = int(input())
discount_percent = int(input()) / 100

total_cost = (pen_packages * PEN_PACKAGE_PRICE) + (marker_packages * MARKER_PACKAGE_PRICE) + (detergent_liters * DETERGENT_PRICE)

discount = total_cost * discount_percent

final_price = total_cost - discount

print(final_price)
