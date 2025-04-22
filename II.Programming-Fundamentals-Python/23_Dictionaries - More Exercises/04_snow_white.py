dwarfs = {}

while True:
    line = input()
    if line == "Once upon a time":
        break
    dwarf_name, hat_color, physics = line.split(" <:> ")
    physics = int(physics)

    dwarf_id = (dwarf_name, hat_color)

    if dwarf_id in dwarfs:
        dwarfs[dwarf_id]= max(physics, dwarfs[dwarf_id])
    else:
        dwarfs[dwarf_id] = physics

hat_color_count = {}
for (_, hat_color) in dwarfs.keys():
    if hat_color not in hat_color_count:
        hat_color_count[hat_color] = 0
    hat_color_count[hat_color] += 1

sorted_dwarfs = sorted(
    dwarfs.items(),
    key=lambda x: (-x[1], -hat_color_count[x[0][1]])
)

for (name, hat_color), physics in sorted_dwarfs:
    print(f"({hat_color}) {name} <-> {physics}")
