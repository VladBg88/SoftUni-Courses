budget = float(input())
video_cards = int(input())
processors = int(input())
ram_memory = int(input())

video_card_price_per = 250

video_card_price = video_card_price_per * video_cards
processors_price_per = video_card_price * 0.35
ram_memory_price_per = video_card_price * 0.10

processors_price = processors_price_per * processors
ram_memory_price = ram_memory_price_per * ram_memory

total = ram_memory_price + processors_price + video_card_price

if video_cards > processors:
    total = total * 0.85

if total <= budget:
    reserve = budget - total
    print(f'You have {reserve:.2f} leva left!')
else:
    more_money = total - budget
    print(f'Not enough money! You need {more_money:.2f} leva more!')
