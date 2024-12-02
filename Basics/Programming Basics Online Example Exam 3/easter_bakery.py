flour_kg_price = float(input())
flour_kgs = float(input())
sugar_kgs = float(input())
egg_bags_count = int(input())
maya_packages = int(input())

sugar_price_kg = flour_kg_price - flour_kg_price * 0.25
egg_bag_price = flour_kg_price + flour_kg_price * 0.10
maya_package_price = sugar_price_kg - sugar_price_kg * 0.80

total_price = (flour_kgs * flour_kg_price) + (sugar_kgs * sugar_price_kg)\
  + (egg_bags_count * egg_bag_price) + (maya_packages * maya_package_price)

print(f"{total_price:.2f}")
