litres_of_the_pool = int(input())
debit_of_first_pipe = int(input())
debit_of_second_pipe = int(input())
hours = float(input())

pipe1 = debit_of_first_pipe * hours
pipe2 = debit_of_second_pipe * hours
total_water = pipe1 + pipe2

if litres_of_the_pool >= total_water:
    print(f"The pool is {100 / litres_of_the_pool * total_water:.2f}% full. Pipe 1: {100 / total_water * pipe1:.2f}%. Pipe 2: {100 / total_water * pipe2:.2f}%.")
else:
    print(f"For {hours:.2f} hours the "
          f"pool overflows with {total_water - litres_of_the_pool} liters.")
