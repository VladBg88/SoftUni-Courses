number_of_pairs = int(input())
previous_sum_of_pair = 0
counter_equal_pairs = 0
max_difference = 0
value = 0

for i in range(number_of_pairs):
    a_number = int(input())
    b_number = int(input())
    pairs_sum = a_number + b_number

    if i > 0:
        if pairs_sum == previous_sum_of_pair:
            counter_equal_pairs += 1
            value = pairs_sum
        else:
            difference = abs(previous_sum_of_pair - pairs_sum)
            if difference > max_difference:
                max_difference = difference

    previous_sum_of_pair = pairs_sum
    if number_of_pairs == 1:
        value = pairs_sum

if counter_equal_pairs == number_of_pairs - 1:
    print(f'Yes, value={value}')
else:
    print(f'No, maxdiff={max_difference}')
