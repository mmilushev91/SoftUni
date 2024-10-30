GREENING_SQ_M_PRICE = 7.61
DISCOUNT = 0.18

sq_m = float(input())

total_cost = sq_m * GREENING_SQ_M_PRICE
discount =  total_cost * DISCOUNT

final_price = total_cost - discount

print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount} lv.")
