command = input()

most_points = float("-inf")
most_points_movie = None
counter = 0

while command != "STOP":
    movie_name = command

    counter += 1

    if counter == 7:
        print("The limit is reached.")
        break

    movie_points = 0

    for char in movie_name:
        movie_points += ord(char)
        if char.islower():
            movie_points -= 2 * len(movie_name)
        elif char.isupper():
            movie_points -= len(movie_name)

    if most_points < movie_points:

        most_points = movie_points
        most_points_movie = movie_name

    command = input()

print(f"The best movie for you is {most_points_movie} with {most_points} ASCII sum.")
