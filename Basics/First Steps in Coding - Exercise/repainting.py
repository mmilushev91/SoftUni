NYLON_PRICE = 1.50
PAINT_PRICE = 14.50
DETERGENT_PRICE = 5
BAGS_PRICE = 0.40

ADDED_NYLON = 2
ADDED_PAINT = 0.10

WORK_COST_PERCENT = 0.3

nylon_sq_m = int(input())
paint_l = int(input())
detergent_l = int(input())
work_hours = int(input())

materials_cost = ((nylon_sq_m + ADDED_NYLON) * NYLON_PRICE) + ((paint_l + paint_l * ADDED_PAINT) * PAINT_PRICE) + (detergent_l * DETERGENT_PRICE) + BAGS_PRICE

work_per_hour_price = materials_cost * WORK_COST_PERCENT
total_work_price_cost = work_per_hour_price * work_hours

total_cost = materials_cost + total_work_price_cost

print(total_cost)
