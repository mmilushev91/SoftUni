# Pseudocode

# prompt sq meters to be greened(float)
# init const variable for price sq meter
# calculate total price
# calculate discount (18% from total price)
# calculate final price
# print first line: "The final price is: {крайна цена на услугата} lv."
# print second line: "The discount is: {отстъпка} lv."

sq_meters = float(input())

PRICE_PER_SQ_METER = 7.61

total_price = sq_meters * PRICE_PER_SQ_METER
discount = total_price * 0.18
final_price = total_price - discount

print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount} lv.")
