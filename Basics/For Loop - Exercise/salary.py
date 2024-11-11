PENALTIES = {
    "Facebook": 150,
    "Instagram":  100,
    "Reddit": 50,
}

tabs_count = int(input())
salary = int(input())

for _ in range(tabs_count):
    tab = input()
    
    if tab in PENALTIES:
        penalty = PENALTIES[tab]
        
        salary -= penalty
        
        if salary <= 0:
            
            print("You have lost your salary.")
            break
else:
    print(int(salary))
  
