targets_list = list(map(int, input().split()))
count_shot_targets = 0

while True:
    index_to_shoot = input()
    if index_to_shoot == "End":
        break
    else:
        index_to_shoot = int(index_to_shoot)

    if index_to_shoot not in range(len(targets_list)):
        continue

    current_value = targets_list[index_to_shoot]

    if targets_list[index_to_shoot] != -1:
        targets_list = [
            int(target) - current_value if target > current_value and target != -1 else
            int(target) + current_value if target <= current_value and target != -1 else int(target)
            for target in targets_list
        ]

        targets_list[index_to_shoot] = -1
        count_shot_targets += 1

print(f"Shot targets: {count_shot_targets} -> {' '.join(map(str, targets_list))}")
