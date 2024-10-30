HOURS_PER_PROJECT = 3

name = input()
projects_count = int(input())

total_time_needed = projects_count * HOURS_PER_PROJECT

print(f"The architect {name} will need {total_time_needed} hours to complete {projects_count} project/s.")
