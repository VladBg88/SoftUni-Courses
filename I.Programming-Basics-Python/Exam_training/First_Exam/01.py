PAPER_PRICE = 5.80
TEXTILE_PRICE = 7.20
GLUE_PRICE = 1.20

paper_number = int(input())
textile_number = int(input())
glue_litres = float(input())
percent_promo = 1 - float(input()) / 100

spending = (paper_number * PAPER_PRICE) + (textile_number * TEXTILE_PRICE) + (glue_litres * GLUE_PRICE)
price_plus_discount = spending * percent_promo


print(f"{price_plus_discount:.3f}")
