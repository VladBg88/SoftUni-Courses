painted_eggs = int(input())
red = 0
orange = 0
blue = 0
green = 0

for _ in range(painted_eggs):
    color = str(input())
    if color == 'red':
        red += 1
    elif color == 'orange':
        orange += 1
    elif color == 'blue':
        blue += 1
    elif color == 'green':
        green += 1

color_counts = {
    'red': red,
    'orange': orange,
    'blue': blue,
    'green': green
}

max_color = max(color_counts, key=color_counts.get)

print(f'Red eggs: {red}')
print(f'Orange eggs: {orange}')
print(f'Blue eggs: {blue}')
print(f'Green eggs: {green}')
print(f'Max eggs: {color_counts[max_color]} -> {max_color}')
