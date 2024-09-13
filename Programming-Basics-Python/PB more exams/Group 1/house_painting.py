GREEN_PAINT_CONSUMPTION = 3.4
RED_PAINT_CONSUMPTION = 4.3

x = float(input())
y = float(input())
h = float(input())

side_walls = (x * y - 2.25) * 2
front_back_walls = x * x * 2 - 2.4
walls_total = side_walls + front_back_walls
green_paint = walls_total / GREEN_PAINT_CONSUMPTION

roof_rectangular = 2 * (x * y)
roof_triangles = 2 * (x * h / 2)
roof_total = roof_rectangular + roof_triangles
red_paint = roof_total / RED_PAINT_CONSUMPTION

print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")
