number_of_snowballs = int(input())
weight_best = 0
time_best = 0
quality_best = 0
value_best = 0

for snowballs in range(number_of_snowballs):
    weight = int(input())
    time_to_hit = int(input())
    quality = int(input())

    snowball_value = (weight / time_to_hit) ** quality

    if snowball_value > value_best:
        value_best = snowball_value
        time_best = time_to_hit
        weight_best = weight
        quality_best = quality


print(f'{weight_best} : {time_best} = {value_best:.0f} ({quality_best})')
