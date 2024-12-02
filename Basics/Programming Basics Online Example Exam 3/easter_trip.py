destination_price = {
  "France": {
    "21-23": 30,
    "24-27": 35,
    "28-31": 40,
  },
  
  "Italy": {
    "21-23": 28,
    "24-27": 32,
    "28-31": 39,
  },
  
  "Germany": {
    "21-23": 32,
    "24-27": 37,
    "28-31": 43,
  }  
}

destination = input()
date = input()
nights_count = int(input())

cost = nights_count * destination_price[destination][date]

print(f"Easter trip to {destination} : {cost:.2f} leva.")
