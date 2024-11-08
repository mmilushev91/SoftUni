season = input()
km_per_month = float(input())

price_per_km = 0
price = 0

if km_per_month <= 5000:
    
    if season == "Spring" or season == "Autumn":
        price = 0.75
    
    elif season == "Summer":
        price = 0.90
    
    elif season == "Winter":
        price = 1.05

elif km_per_month <= 10_000:
    
    if season == "Spring" or season == "Autumn":
        price = 0.95
    
    elif season == "Summer":
        price = 1.10
    
    elif season == "Winter":
        price = 1.25

else:
    price = 1.45

payment = (km_per_month * 4) * price

taxes = payment * 0.10

payment -= taxes

print(f"{payment:.2f}")
