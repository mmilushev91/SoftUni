SEAT_HEIGHT = 120
SEAT_WIDTH = 70
TAKEN_SPACE = 3

height = float(input()) * 100
width = (float(input()) * 100) - 100

column_seats = height // SEAT_HEIGHT
row_seats = width // SEAT_WIDTH

seats = int(row_seats * column_seats) - TAKEN_SPACE

print(seats)
