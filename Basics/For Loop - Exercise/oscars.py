WIN_LIMIT = 1250.5

actor_name = input()
academy_points = float(input())
judges_count = int(input())

actor_points = academy_points

for _ in range(judges_count):
    judge_name = input()
    judge_points = float(input())
    
    name_points = len(judge_name)
    
    points = (judge_points * name_points )/ 2
  
    actor_points += points
    
    print(actor_points)
    
    if actor_points > WIN_LIMIT:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {actor_points:.1f}!")
        break
    
else:
    points_needed = WIN_LIMIT - actor_points
    
    print(f"Sorry, {actor_name} you need {points_needed:.1f} more!")
  
