DEF_DAMAGE = 45
DEF_HEALTH = 250
DEF_ARMOR = 10
container_dragons = {}

number_of_dragons = int(input())

# Reading the dragon data
for dragon in range(number_of_dragons):
    user_input = str(input()).split()
    dragon_type, dragon_name = user_input[0], user_input[1]

    # Handling 'null' values and replacing them with defaults
    if user_input[2] == 'null':
        user_input[2] = DEF_DAMAGE
    if user_input[3] == 'null':
        user_input[3] = DEF_HEALTH
    if user_input[4] == 'null':
        user_input[4] = DEF_ARMOR

    damage, health, armor = int(user_input[2]), int(user_input[3]), int(user_input[4])

    # Creating the dragon dictionary
    new_dragon = {
        'damage': damage,
        'health': health,
        'armor': armor
    }

    # Adding dragon to the container
    if dragon_type not in container_dragons:
        container_dragons[dragon_type] = {}

    container_dragons[dragon_type][dragon_name] = new_dragon

# Calculating and printing the averages for each dragon type
for dragon_type, dragons in container_dragons.items():
    total_damage = 0
    total_health = 0
    total_armor = 0
    dragon_count = len(dragons)

    # Summing up the stats for each dragon under this type
    for dragon_name, stats in dragons.items():
        total_damage += stats['damage']
        total_health += stats['health']
        total_armor += stats['armor']

    # Calculating the averages
    average_damage = total_damage / dragon_count
    average_health = total_health / dragon_count
    average_armor = total_armor / dragon_count

    # Printing the average stats for the dragon type
    print(f"{dragon_type}::({average_damage:.2f}/{average_health:.2f}/{average_armor:.2f})")

    sorted_dragons = sorted(dragons.items(), key=lambda x: x[0])

    # Printing individual dragons and their stats
    for dragon_name, stats in sorted_dragons:
        print(f"-{dragon_name} -> damage: {int(stats['damage'])}, health: {int(stats['health'])}, armor: {int(stats['armor'])}")
