rounds = int(input())

score = 0
group_one, group_two, group_three, group_fourth, group_fifth, group_six = 0, 0, 0, 0, 0, 0

for _ in range(rounds):
  number = int(input())
  
  if number < 0 or number > 50:
    group_six += 1
    score /= 2
    continue
  
  if number < 10:
    group_one += 1 
    score += number * 0.20 
  
  elif number < 20:
    group_two += 1 
    score += number * 0.30 
  
  elif number < 30:
    group_three += 1 
    score += number * 0.40 
    
  elif number < 40:
    group_fourth += 1 
    score += 50
  
  elif number <= 50:
    group_fifth += 1 
    score += 100
    
print(f"{score:.2f}")
print(f"From 0 to 9: {group_one / rounds * 100:.2f}%")
print(f"From 10 to 19: {group_two / rounds * 100:.2f}%")
print(f"From 20 to 29: {group_three / rounds * 100:.2f}%")
print(f"From 30 to 39: {group_fourth / rounds * 100:.2f}%")
print(f"From 40 to 50: {group_fifth / rounds * 100:.2f}%")
print(f"Invalid numbers: {group_six / rounds * 100:.2f}%")
