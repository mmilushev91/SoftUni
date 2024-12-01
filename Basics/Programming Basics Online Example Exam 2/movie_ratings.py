movies_count = int(input())

total_rating = 0
max_rating = float("-inf")
min_rating = float("inf")
max_rating_movie = None
min_rating_movie = None

for _ in range(movies_count):
    movie = input()
    rating = float(input())

    total_rating += rating

    if rating > max_rating:
        max_rating = rating
        max_rating_movie = movie

    if rating < min_rating:
        min_rating = rating
        min_rating_movie = movie

average_rating = total_rating / movies_count

print(f"{max_rating_movie} is with highest rating: {max_rating:.1f}")
print(f"{min_rating_movie} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")
