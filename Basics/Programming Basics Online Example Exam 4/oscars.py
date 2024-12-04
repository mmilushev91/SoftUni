NOMINE_POINTS = 1250.5

actor_name = input()
academy_points = float(input())
judges_count = int(input())

actor_points = academy_points

for _ in range(judges_count):
    judge_name = input()
    judge_points = float(input())

    judge_final_points = (len(judge_name) * judge_points) / 2

    actor_points += judge_final_points

    if actor_points >= NOMINE_POINTS:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {actor_points:.1f}!")
        break

else:
    points_needed = NOMINE_POINTS - actor_points
    
    print(f"Sorry, {actor_name} you need {points_needed:.1f} more!")
  
