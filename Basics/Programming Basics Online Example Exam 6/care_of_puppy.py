bought_food = int(input()) * 1000

command = input()

food_eaten = 0

while command != "Adopted":
    daily_food_eaten = int(command)

    food_eaten += daily_food_eaten

    command = input()

if bought_food >= food_eaten:
    left_food = bought_food - food_eaten

    print(f"Food is enough! Leftovers: {left_food} grams." )

else:
    food_needed = food_eaten - bought_food

    print(f"Food is not enough. You need {food_needed} grams more.")
