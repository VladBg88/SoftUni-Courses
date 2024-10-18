initial_energy = int(input())
won_battles = 0

while True:
    enemy_distance = input()

    if enemy_distance == 'End of battle':
        print(f"Won battles: {won_battles}. Energy left: {initial_energy}")
        break

    if initial_energy >= int(enemy_distance):
        initial_energy -= int(enemy_distance)
        won_battles += 1
        if won_battles % 3 == 0:
            initial_energy += won_battles
    else:
        print(f"Not enough energy! Game ends with {won_battles} won battles and {initial_energy} energy")
        break
