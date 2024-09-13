def warn_the_sheep():
    # Take input from the user
    queue = input("Enter the animals in the queue (e.g. 'sheep, sheep, wolf'): ")

    # Split the input string into a list of animals
    animals = queue.split(", ")

    # Find the position of the wolf in the list
    wolf_position = animals.index("wolf")

    # Check if the wolf is at the end of the list (closest to the farmer)
    if wolf_position == len(animals) - 1:
        print("Please go away and stop eating my sheep")
    else:
        # Calculate how many sheep are in danger
        sheep_in_danger = len(animals) - wolf_position - 1
        print(f"Oi! Sheep number {sheep_in_danger}! You are about to be eaten by a wolf!")


# Run the function
warn_the_sheep()
