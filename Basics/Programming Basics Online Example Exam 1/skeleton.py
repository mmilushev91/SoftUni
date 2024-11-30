time_to_beat_seconds = int(input()) * 60 + int(input())

distance_meters = float(input())
seconds_per_100_meters = int(input())

marin_time = (distance_meters / 100) * seconds_per_100_meters
time_to_remove = (distance_meters / 120) * 2.5

marin_time -= time_to_remove

if marin_time <= time_to_beat_seconds:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {marin_time:.3f}.")
else:
    time_needed = marin_time - time_to_beat_seconds
    print(f"No, Marin failed! He was {time_needed:.3f} second slower.")
