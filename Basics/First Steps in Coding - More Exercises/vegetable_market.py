EURO = 1.94

vegetables_price = float(input())
fruits_price = float(input())

vegetables_kg= int(input())
fruits_kg= int(input())

bgn_income = (vegetables_price * vegetables_kg) + (fruits_price * fruits_kg)

euro_income = bgn_income / EURO

print(f"{euro_income:.2f}")
