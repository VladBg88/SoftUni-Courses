PEN_PACK_PRICE = 5.80
MARKER_PACK_PRICE = 7.20
DETERGENT_LITRE_PRICE = 1.20

pen_packs = int(input())
marker_packs = int(input())
litres_detergent = int(input())
discount_percent = int(input()) / 100

pens_total = pen_packs * PEN_PACK_PRICE
markers_total = marker_packs * MARKER_PACK_PRICE
detergent_total = litres_detergent * DETERGENT_LITRE_PRICE
total = pens_total + markers_total + detergent_total

discounted_total = total - (total * discount_percent)

print(discounted_total)