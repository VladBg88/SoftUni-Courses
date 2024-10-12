number_of_electrons = int(input())
shells_list = []
shell_count = 1
while True:
    shell_capacity = 2 * (shell_count ** 2)
    if number_of_electrons >= shell_capacity:
        shells_list.append(shell_capacity)
        number_of_electrons -= shell_capacity
        shell_count += 1
    else:
        if number_of_electrons != 0:
            shells_list.append(number_of_electrons)
        break

print(shells_list)