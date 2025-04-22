from collections import deque

PRICE_TOYS = {
    "Doll": 150,
    "Wooden train": 250,
    "Teddy bear": 300,
    "Bicycle": 400
}

materials = deque(map(int, input().split())) #last_element
magic = deque(map(int, input().split())) #first_element
christmas = False

crafted_toys = {}

while materials and magic:

    if materials[-1] == 0 and magic[0] == 0:
        materials.pop()
        magic.popleft()
        continue
    elif materials[-1] == 0:
        materials.pop()
        continue
    elif magic[0] == 0:
        magic.popleft()
        continue

    last_box = materials.pop()
    first_magic = magic.popleft()
    total_magic = last_box * first_magic

    if total_magic in PRICE_TOYS.values(): #If total_magic equals one of the levels described in PRICE_TOYS
        key = next(key for key, value in PRICE_TOYS.items() if value == total_magic)
        crafted_toys[key] = crafted_toys.get(key, 0) + 1
        if ("Doll" in crafted_toys and "Wooden train" in crafted_toys) or \
                ("Teddy bear" in crafted_toys and "Bicycle" in crafted_toys):
            christmas = True
        continue
    elif total_magic < 0: #If the result is negative
        materials.append(last_box + first_magic)
    else:
        materials.append(last_box + 15)

if christmas:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(map(str, reversed(materials)))}")
if magic:
    print(f"Magic left: {', '.join(map(str, magic))}")

for toy, amount in sorted(crafted_toys.items()):
    print(f"{toy}: {amount}")