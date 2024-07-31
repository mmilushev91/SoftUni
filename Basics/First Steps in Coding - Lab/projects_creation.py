# Pseudocode

# prompt user for architect name (string) and number of projects (int)
# init const variable for completing one project(3 hours)
# calculate time needed to complete projects
# print f string: "The architect {името на архитекта} will need {необходими часове} hours to complete {брой на проектите} project/s."

name = input()
projects_count = int(input())

HOURS_PER_PROJECT = 3

total_time_needed = projects_count * HOURS_PER_PROJECT

print(f"The architect {name} will need {total_time_needed} hours to complete {projects_count} project/s.")
