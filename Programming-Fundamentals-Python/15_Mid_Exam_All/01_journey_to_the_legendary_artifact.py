def journey_to_the_legendary_artifact():
    initial_energy = float(input())
    terrains = []
    warrior_energy = initial_energy
    artifact_pieces = 0
    mountains_passed = 0

    while True:
        command = input()
        if command == "Journey ends here!":
            break

        terrains.append(command)

    for terrain in terrains:
        if terrain == "mountain":
            mountains_passed += 1
            warrior_energy -= 10
            if mountains_passed % 3 == 0:
                artifact_pieces += 1

            if artifact_pieces == 3:
                print(f"The character reached the legendary artifact with {warrior_energy:.2f} warrior_energy left.")
                return

        elif terrain == "desert":
            warrior_energy -= 15

        elif terrain == "forest":
            warrior_energy += 7

        if warrior_energy <= 0:
            print("The character is too exhausted to carry on with the journey.")
            return

    if artifact_pieces < 3:
        missing_pieces = 3 - artifact_pieces
        print(f"The character could not find all the pieces and needs {missing_pieces} more to complete the legendary "
              f"artifact.")


journey_to_the_legendary_artifact()
