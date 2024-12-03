days_count = int(input()) + 1
food = float(input())

total_food_eaten, total_food_eaten_by_dog, total_food_eaten_by_cat = 0, 0, 0
eaten_biscuits = 0

for day in range(1, days_count):
    eat_food_by_dog = int(input())
    eat_food_by_cat = int(input())

    total_food_eaten_by_dog += eat_food_by_dog
    total_food_eaten_by_cat += eat_food_by_cat

    if day % 3 == 0:
        eaten_biscuits += (eat_food_by_dog + eat_food_by_cat) * 0.10

total_food_eaten = total_food_eaten_by_dog + total_food_eaten_by_cat

print(f"Total eaten biscuits: {round(eaten_biscuits)}gr.")
print(f"{total_food_eaten / food * 100:.2f}% of the food has been eaten.")
print(f"{total_food_eaten_by_dog / total_food_eaten * 100:.2f}% eaten from the dog.")
print(f"{total_food_eaten_by_cat / total_food_eaten * 100:.2f}% eaten from the cat.")
