# Pseudocode

# prompt user for book_pages(int), pages_per_hour(int), days(itn)
# calculate hours_per_day with formula (book_pages / days) / pages_per_hour and trunc the result
# print result

book_pages = int(input())
days = int(input())
pages_per_hour = int(input())

hours_per_day = int((book_pages / days) / pages_per_hour)

print(hours_per_day)
