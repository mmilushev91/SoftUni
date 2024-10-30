pages_to_read = int(input())
pages_per_hour = int(input())
days_to_read = int(input())

pages_per_day = pages_to_read / days_to_read

hours_per_day = pages_per_day / pages_per_hour

print(int(hours_per_day))
