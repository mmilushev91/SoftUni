easter_cake_count = int(input())
egg_bags_count = int(input())
cookies_kg = int(input())

total_price = (easter_cake_count * 3.20) + (egg_bags_count * 4.35) + (cookies_kg * 5.40) + (egg_bags_count * 12 * 0.15)

print(f"{total_price:.2f}")
