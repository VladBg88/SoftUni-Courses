days_of_tournaments = int(input())

total_win_count = 0
total_loss_count = 0

day_win_count = 0
day_loss_count = 0

day_earned_money = 0
total_earning = 0


for i in range(days_of_tournaments):
    while True:
        sport = str(input())
        if sport == 'Finish':
            if day_win_count > day_loss_count:
                day_earned_money *= 1.1
                total_earning += day_earned_money
            else:
                total_earning += day_earned_money
            day_win_count = 0
            day_loss_count = 0
            day_earned_money = 0
            break

        result = str(input())

        if result == 'win':
            total_win_count += 1
            day_win_count += 1
            day_earned_money += 20
            # total_earning += 20
        elif result == 'lose':
            total_loss_count += 1
            day_loss_count += 1

if total_win_count > total_loss_count:
    total_earning *= 1.2
    print(f'You won the tournament! Total raised money: {total_earning:.2f}')
else:
    print(f'You lost the tournament! Total raised money: {total_earning:.2f}')
