budget_for_actors = float(input())
spending = 0
budget_left = budget_for_actors

while True:
    name_of_actor = input()
    if name_of_actor == 'ACTION':
        break

    if len(name_of_actor) > 15:
        spending += budget_left * 0.2
        budget_left -= budget_left * 0.2
    else:
        salary = float(input())
        spending += salary
        budget_left -= salary

    if spending > budget_for_actors:
        print(f'We need {spending - budget_for_actors:.2f} leva for our actors.')
        break

if budget_for_actors >= spending:
    print(f'We are left with {budget_for_actors - spending:.2f} leva.')
