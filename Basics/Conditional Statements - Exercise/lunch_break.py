from math import ceil

NOT_WATCHTING = 0.375

series = input()

series_length = int(input())
lunck_break_length = int(input())

lunck_break_left = lunck_break_length * NOT_WATCHTING

lunck_break_length -= lunck_break_left

if lunck_break_length >= series_length:
  lunck_break_length -= series_length
  
  print(f"You have enough time to watch {series} and left with {ceil(lunck_break_length)} minutes free time.")

else:
  needed_time = series_length - lunck_break_length
  
  print(f"You don't have enough time to watch {series}, you need {ceil(needed_time)} more minutes.")
  
