
room_tax = int(input())

prize_figures_price = room_tax * 0.7
catering_price = prize_figures_price * 0.85
sound_price = catering_price / 2

total_sum = room_tax + prize_figures_price + catering_price + sound_price
print(f"{total_sum:.2f}")
