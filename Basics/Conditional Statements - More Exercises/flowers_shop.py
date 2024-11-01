from math import ceil, floor

MAGNOLIAS_PRICE = 3.25
ZUMBULI_PRICE = 4
ROSES_PRICE = 3.50
CACTI_PRICE = 8

TAXES = 0.05

magnolias_count = int(input())
zumbuli_count = int(input())
roses_count = int(input())
cacti_count = int(input())

gift_price = float(input())

income = (magnolias_count * MAGNOLIAS_PRICE) + (zumbuli_count * ZUMBULI_PRICE) + (roses_count * ROSES_PRICE) + (cacti_count * CACTI_PRICE)

taxes = income * TAXES

income -= taxes

if income >= gift_price:
  left_money = income - gift_price
  
  print(f"She is left with {floor(left_money)} leva." )

else:
  needed_money = gift_price - income
  print(f"She will have to borrow {ceil(needed_money)} leva." )
  
