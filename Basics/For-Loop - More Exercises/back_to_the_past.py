START_YEAR = 1800

inhrerited_money = float(input())
year_to_live = int(input())

age = 18

for year in range(START_YEAR, year_to_live + 1):
  
  if year % 2 == 0:
    inhrerited_money -= 12000
  else:
    inhrerited_money -= 12000 + 50 * age
    
  age += 1

if inhrerited_money >= 0:
  print(f"Yes! He will live a carefree life and will have {inhrerited_money:.2f} dollars left." )

else:
  print(f"He will need {abs(inhrerited_money):.2f} dollars to survive.")
  
