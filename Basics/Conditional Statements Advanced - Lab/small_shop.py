city_prices = {
    "Sofia": {
        "coffee": 0.50,
        "water": 0.80,
        "beer": 1.20,
        "sweets": 1.45,
        "peanuts": 1.60,
    },
    
    "Plovdiv": {
        "coffee": 0.40,
        "water": 0.70,
        "beer": 1.15,
        "sweets": 1.30,
        "peanuts": 1.50,
    },
    
     "Varna": {
        "coffee": 0.45,
        "water": 0.70,
        "beer": 1.10,
        "sweets": 1.35,
        "peanuts": 1.55,
    }
}

product = input()
city = input()
quantiy = float(input())

cost = quantiy * city_prices[city][product]

print(cost)
