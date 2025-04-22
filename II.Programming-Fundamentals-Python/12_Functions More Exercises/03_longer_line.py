from math import sqrt
from math import floor


def calculate_distance(x1, y1, x2, y2):
    # Function to calculate the length of the line segment
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def point_distance_from_origin(x, y):
    # Function to calculate the distance of a point from the origin
    return sqrt(x ** 2 + y ** 2)


def print_closer_first(x1, y1, x2, y2):
    # Function to print the points in order, starting from the one closer to the origin
    if point_distance_from_origin(x1, y1) <= point_distance_from_origin(x2, y2):
        print(f"({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})")
    else:
        print(f"({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})")


def longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    # Calculate the lengths of both lines
    line1_length = calculate_distance(x1, y1, x2, y2)
    line2_length = calculate_distance(x3, y3, x4, y4)

    # Compare the lengths and print the longer one
    if line1_length >= line2_length:
        print_closer_first(x1, y1, x2, y2)
    else:
        print_closer_first(x3, y3, x4, y4)


# Input example
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

# Call the function with the given coordinates
longer_line(x1, y1, x2, y2, x3, y3, x4, y4)
