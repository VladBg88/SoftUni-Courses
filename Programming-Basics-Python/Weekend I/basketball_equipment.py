BASKETBALL_SHOES_RATE_DECREASE = 40/100
BASKETBALL_CLOTHES_RATE_DECREASE = 20/100
BASKETBALL_BALL_RATE = 1/4
BASKETBALL_ACCESSORIES_RATE = 1/5

yearly_price = int(input())

shoes_price = yearly_price - (yearly_price * BASKETBALL_SHOES_RATE_DECREASE)
clothes_price = shoes_price - (shoes_price * BASKETBALL_CLOTHES_RATE_DECREASE)
ball_price = clothes_price * BASKETBALL_BALL_RATE
accessories_price = ball_price * BASKETBALL_ACCESSORIES_RATE

total_price = yearly_price + shoes_price + ball_price +accessories_price + clothes_price

print(total_price)
