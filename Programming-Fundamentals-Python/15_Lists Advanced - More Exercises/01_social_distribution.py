population_list = list(map(int, input().split(', ')))
minimum_wealth = int(input())

while True:
    if min(population_list) >= minimum_wealth:
        print(population_list)
        break
    elif max(population_list) == minimum_wealth:
        print(f"No equal distribution possible")
        break

    for index, num_1 in enumerate(population_list):
        if max(population_list) >= minimum_wealth:
            if num_1 < minimum_wealth:
                max_num = max(population_list)
                index_of_max = population_list.index(max_num)
                needed = minimum_wealth - population_list[index]
                redundant = population_list[index_of_max] - minimum_wealth
                if redundant >= needed:
                    shared = needed
                else:
                    shared = redundant
                population_list[index] += shared
                population_list[index_of_max] -= shared
        else:
            break
