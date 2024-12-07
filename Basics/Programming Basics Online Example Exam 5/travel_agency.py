first_group_prices = {
  "noEquipment":  [80, 0.05],
  "withEquipment": [100, 0.1],
}

second_group_prices = {
  "noBreakfast":  [100, 0.07],
  "withBreakfast": [130, 0.12],
}

cities = ["Bansko",  "Borovets", "Varna", "Burgas"]

city = input()
package_type = input()
discount = input()
nights = int(input())

if nights < 1:
  print("Days must be positive number!")
  quit()

if city not in cities or (package_type not in first_group_prices and package_type not in second_group_prices):
  print("Invalid input!")
  quit()

single_price = 0
discount_percent = 0

if nights > 7:
  nights -= 1

if city == "Bansko" or city == "Borovets":
  single_price = first_group_prices[package_type][0]
  discount_percent = first_group_prices[package_type][1]
else:
  single_price = second_group_prices[package_type][0]
  discount_percent = second_group_prices[package_type][1]

total_price = single_price * nights

if discount == "yes":
  total_price *= 1 - discount_percent

print(f"The price is {total_price:.2f}lv! Have a nice time!")
