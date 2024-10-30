GREEN_PAINT_CONSUMPTION = 3.4
RED_PAINT_CONSUMPTION = 4.3

FRONT_SIDE_DOOR = 2.4
SIDES_WINDOWS = 4.5

x = float(input())
y = float(input())
h = float(input())

REACTANGLE_SIDES = 2 * (x * y)
SQUARE_SIDES = 2 * x**2
ROOF_TRIANGLE_SIDES = 2 * ((x * h) / 2)

front_sides_green_paint = SQUARE_SIDES - FRONT_SIDE_DOOR

side_sides_green_paint = REACTANGLE_SIDES - SIDES_WINDOWS

green_paint_total = (front_sides_green_paint +
                     side_sides_green_paint) / GREEN_PAINT_CONSUMPTION

red_paint_total = (REACTANGLE_SIDES + ROOF_TRIANGLE_SIDES) / RED_PAINT_CONSUMPTION

print(f"{green_paint_total:.2f}")
print(f"{red_paint_total:.2f}")
