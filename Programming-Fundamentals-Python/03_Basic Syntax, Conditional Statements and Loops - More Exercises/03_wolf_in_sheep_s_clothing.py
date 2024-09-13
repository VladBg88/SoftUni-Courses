def warn_the_sheep():
    queue = input()

    animals = queue.split(", ")

    wolf_position = animals.index("wolf")

    if wolf_position == len(animals) - 1:
        print("Please go away and stop eating my sheep")
    else:
        sheep_in_danger = len(animals) - wolf_position - 1
        print(f"Oi! Sheep number {sheep_in_danger}! You are about to be eaten by a wolf!")


warn_the_sheep()
