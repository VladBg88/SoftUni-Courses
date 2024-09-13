desired_earning = float(input())
earning = 0

while True:
    name_of_cocktail = str(input())
    if name_of_cocktail == 'Party!':
        print(f'We need {desired_earning - earning:.2f} leva more.')
        break

    number_of_cocktails = int(input())

    price = len(name_of_cocktail) * number_of_cocktails
    if price % 2 == 1:
        price *= 0.75

    earning += price

    if earning >= desired_earning:
        print(f'Target acquired.')
        break


print(f'Club income - {earning:.2f} leva.')
