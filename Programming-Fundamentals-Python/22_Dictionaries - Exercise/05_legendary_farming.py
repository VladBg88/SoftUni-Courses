key_materials = {'shards': 0, 'fragments': 0, 'motes': 0}
junk = {}
stop_point = False

while True:
    if stop_point:
        break

    raw_data = input().split()

    for i in range(0, len(raw_data), 2):
        quantity = int(raw_data[i])
        material = raw_data[i + 1].lower()
        if material in ('shards', 'fragments', 'motes'):
            key_materials[material] += quantity
            if key_materials[material] >= 250:
                key_materials[material] -= 250
                if material == 'shards':
                    print("Shadowmourne obtained!")
                elif material == 'fragments':
                    print("Valanyr obtained!")
                elif material == 'motes':
                    print("Dragonwrath obtained!")

                print(f"shards: {key_materials['shards']}")
                print(f"fragments: {key_materials['fragments']}")
                print(f"motes: {key_materials['motes']}")

                for material, quantity in junk.items():
                    print(f"{material}: {quantity}")
                stop_point = True
                break

        else:
            if material in junk:
                junk[material] += quantity
            else:
                junk[material] = quantity
