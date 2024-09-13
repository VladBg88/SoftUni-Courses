celsius = float(input())
time_of_day = str(input())
outfit = ""

if 10 <= celsius <= 18:
    if time_of_day == "Morning":
        outfit = " Sweatshirt and Sneakers."
    if time_of_day == "Afternoon":
        outfit = " Shirt and Moccasins."
    if time_of_day == "Evening":
        outfit = " Shirt and Moccasins."
elif 18 < celsius <= 24:
    if time_of_day == "Morning":
        outfit = " Shirt and Moccasins."
    if time_of_day == "Afternoon":
        outfit = " T-Shirt and Sandals."
    if time_of_day == "Evening":
        outfit = " Shirt and Moccasins."
elif celsius >= 25:
    if time_of_day == "Morning":
        outfit = " T-Shirt and Sandals."
    if time_of_day == "Afternoon":
        outfit = " Swim Suit and Barefoot."
    if time_of_day == "Evening":
        outfit = " Shirt and Moccasins."

print(f"It's {celsius:.0f} degrees, get your{outfit}")
