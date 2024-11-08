CHAR_POINTS = {
    "a": 1,
    "e": 2,
    "i": 3,
    "o": 4,
    "u": 5,
}

string = input()

points = 0

for char in string:
    
    if char in CHAR_POINTS:
        points += CHAR_POINTS[char]

print(points)
