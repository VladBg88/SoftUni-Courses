purchased_chrysanthemums = int(input())
purchased_roses = int(input())
purchased_tulips = int(input())
season = str(input())
special_day = str(input())
chrysanthemums_price = 0
roses_price = 0
tulips_price = 0
arranging_flowers_tax = 2

if season == 'Spring' or season == 'Summer':
    chrysanthemums_price = 2.00
    roses_price = 4.10
    tulips_price = 2.50
elif season == 'Autumn' or season == 'Winter':
    chrysanthemums_price = 3.75
    roses_price = 4.50
    tulips_price = 4.15

chrysanthemums_total = chrysanthemums_price * purchased_chrysanthemums
roses_total = roses_price * purchased_roses
tulip_total = tulips_price * purchased_tulips
total_price = chrysanthemums_total + roses_total + tulip_total

if special_day == 'Y':
    total_price *= 1.15

if purchased_tulips > 7 and season == "Spring":
    total_price *= 0.95

if purchased_roses >= 10 and season == "Winter":
    total_price *= 0.9

if purchased_chrysanthemums + purchased_roses + purchased_tulips > 20:
    total_price *= 0.8

print(f"{total_price + arranging_flowers_tax:.2f}")
