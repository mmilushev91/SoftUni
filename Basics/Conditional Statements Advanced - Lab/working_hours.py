CLOSED = "Sunday"

START_HOUR = 10
END_HOUR = 18

hour = int(input())
day = input()


if day == CLOSED or hour < START_HOUR or hour > END_HOUR:
    print("closed")
else:
    print("open")
  
