RUSSIA_RIBOON = 9.100 + 9.400
RUSSIA_HOOP = 9.300 + 9.800
RUSSIA_ROPE = 9.600 + 9.000
BULGARIA_RIBBON = 9.600 + 9.400
BULGARIA_HOOP = 9.550 + 9.750
BULGARIA_ROPE = 9.500 + 9.400
ITALY_RIBBON = 9.200 + 9.500
ITALY_HOOP = 9.450 + 9.350
ITALY_ROPE = 9.700 + 9.150

country = str(input())
tool = str(input())
points = 0

if country == "Russia":
    if tool == "ribbon":
        points = RUSSIA_RIBOON
    elif tool == "hoop":
        points = RUSSIA_HOOP
    else:
        points = RUSSIA_ROPE
elif country == "Bulgaria":
    if tool == "ribbon":
        points = BULGARIA_RIBBON
    elif tool == "hoop":
        points = BULGARIA_HOOP
    else:
        points = BULGARIA_ROPE
elif country == "Italy":
    if tool == "ribbon":
        points = ITALY_RIBBON
    elif tool == "hoop":
        points = ITALY_HOOP
    else:
        points = ITALY_ROPE

print(f"The team of {country} get {points:.3f} on {tool}.")
print(f"{100 - (points * 5):.2f}%")
