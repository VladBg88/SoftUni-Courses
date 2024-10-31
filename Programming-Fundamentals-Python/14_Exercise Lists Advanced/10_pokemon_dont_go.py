def pokemon_app():
    all_pokemons = list(map(int, input().split()))
    all_captured_pokemons = 0

    while all_pokemons:
        command = int(input())
        if command < 0:  # If the given index is less than 0
            captured_pokemon = all_pokemons.pop(0)
            moved_pokemon = all_pokemons[-1]
            all_pokemons.insert(0, moved_pokemon)
        elif command > len(all_pokemons) - 1:  # If the given index is greater than the last index
            captured_pokemon = all_pokemons.pop(-1)
            moved_pokemon = all_pokemons[0]
            all_pokemons.append(moved_pokemon)
        else:
            captured_pokemon = all_pokemons.pop(command)

        all_captured_pokemons += captured_pokemon

        for left_pokemon in range(len(all_pokemons)):
            if all_pokemons[left_pokemon] <= captured_pokemon:
                all_pokemons[left_pokemon] += captured_pokemon
            else:
                all_pokemons[left_pokemon] -= captured_pokemon

    print(all_captured_pokemons)


pokemon_app()
