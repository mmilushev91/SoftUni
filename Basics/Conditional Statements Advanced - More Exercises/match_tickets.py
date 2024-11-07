TICKET_PRICES = {
    "VIP": 499.99,
	"Normal": 249.99,
}

budget = float(input())
ticket_type = input()
group_size = int(input())

transport = 0

if group_size < 5:
    transport = budget * 0.75
    
elif group_size < 10:
    transport = budget * 0.60
    
elif group_size < 25:
    transport = budget * 0.50
    
elif group_size < 50:
    transport = budget * 0.40
    
else:
    transport = budget * 0.25

total_cost = (group_size * TICKET_PRICES[ticket_type]) + transport

if budget >= total_cost:
    money_left = budget - total_cost
    
    print(f"Yes! You have {money_left:.2f} leva left.")
    
else:
    money_needed = total_cost - budget
    
    print(f"Not enough money! You need {money_needed:.2f} leva.")
  
