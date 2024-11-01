LIMITATION = 0

LOW_LIMIT = -100
UP_LIMIT = 100

num = int(input())

if num != LIMITATION and LOW_LIMIT <= num <= UP_LIMIT:
    print("Yes")
else:
    print("No")
