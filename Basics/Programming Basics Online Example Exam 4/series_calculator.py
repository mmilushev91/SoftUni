series_name = input()
seasons_count = int(input())
episodes_count = int(input())
episode_length = int(input())

total_episode_length = (episodes_count * (episode_length * 1.20))
total_length = (total_episode_length + 10) * seasons_count


print(f"Total time needed to watch the {series_name} series is {int(total_length)} minutes.")
