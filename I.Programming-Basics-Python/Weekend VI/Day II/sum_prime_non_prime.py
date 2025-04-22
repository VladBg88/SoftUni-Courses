STOP_STRING = 'stop'

sum_primes = 0
sum_non_primes = 0

while True:
    current_number = input()
    if current_number == STOP_STRING:
        break

    current_number = int(current_number)
    if current_number < 0:
        print('Number is negative.')
        continue

    for number_counter in range(2, current_number + 1):
        if current_number % number_counter == 0 and current_number != number_counter:
            sum_non_primes += current_number
            break
        if current_number == number_counter:
            sum_primes += current_number

print(f'Sum of all prime numbers is: {sum_primes}')
print(f'Sum of all non prime numbers is: {sum_non_primes}')
