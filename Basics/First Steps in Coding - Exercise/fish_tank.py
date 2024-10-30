length = int(input())
width = int(input())
height = int(input())
percent = float(input()) / 100

volume = (length * width * height) / 1000
taken_space = volume * percent

liters = volume - taken_space

print(liters)
