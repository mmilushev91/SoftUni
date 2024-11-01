TYPES = {
    "fruit": ["banana", "apple", "kiwi", "cherry", "lemon", "grapes"],
    "vegetable": ["tomato", "cucumber", "pepper", "carrot"]
}

product = input()

for item in TYPES:
    
    if product in TYPES[item]:
        print(item)
        break
else:
    print("unknown")
