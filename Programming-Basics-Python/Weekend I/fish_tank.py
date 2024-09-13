length = int(input())
width = int(input())
height = int(input())
percent = float(input()) / 100

volume = length * width * height
liters = volume / 1000
needed_liters = liters * (1 - percent)

print(needed_liters)