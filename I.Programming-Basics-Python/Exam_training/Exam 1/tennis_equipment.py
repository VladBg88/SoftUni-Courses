import math

racket_price_per = float(input())
racket_number = int(input())
shoes = int(input())

racket_total_price = racket_number * racket_price_per
shoes_total_price = shoes * (racket_price_per / 6)
equipment_price = (shoes_total_price + racket_total_price) * 0.2
final_price = racket_total_price + shoes_total_price + equipment_price

joko_price = final_price / 8
sponsors_price = final_price * (7 / 8)

print(f"Price to be paid by Djokovic {math.floor(joko_price)}")
print(f"Price to be paid by sponsors {math.ceil(sponsors_price)}")
