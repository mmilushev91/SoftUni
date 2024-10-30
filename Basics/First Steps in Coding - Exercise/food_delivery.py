CHICKEN_MENU_PRICE = 10.35
FISH_MENU_PRICE = 12.40
VEGETARIAN_MENU_PRICE = 8.15
DELIVERY = 2.5
DESERT = 0.20

chicken_menus = int(input())
fish_menus = int(input())
vegetarian_menus = int(input())

total_cost = (chicken_menus * CHICKEN_MENU_PRICE) + (fish_menus * FISH_MENU_PRICE) + (vegetarian_menus * VEGETARIAN_MENU_PRICE)

desert_price = total_cost * DESERT

final_price = total_cost + desert_price + DELIVERY

print(final_price)
