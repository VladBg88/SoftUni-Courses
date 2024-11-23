number_of_pieces = int(input())
all_data = {}
for piece in range(number_of_pieces):
    command = input().split('|')
    piece_name, composer, key = command
    all_data[piece_name] = [composer, key]

while True:
    command = input()
    if command == "Stop":
        for piece, data in all_data.items():
            print(f"{piece} -> Composer: {data[0]}, Key: {data[1]}")
        break
    command = command.split('|')
    if command[0] == "Add":
        new_piece = command[1]
        new_composer = command[2]
        new_key = command[3]
        if new_piece in all_data:
            print(f"{new_piece} is already in the collection!")
            continue
        all_data[new_piece] =[new_composer, new_key]
        print(f"{new_piece} by {new_composer} in {new_key} added to the collection!")
    elif command[0] == "Remove":
        piece_to_remove = command[1]
        if piece_to_remove not in all_data:
            print(f"Invalid operation! {piece_to_remove} does not exist in the collection.")
            continue
        all_data.pop(piece_to_remove)
        print(f"Successfully removed {piece_to_remove}!")
    elif command[0] == "ChangeKey":
        piece_to_change = command[1]
        new_key = command[2]
        if piece_to_change not in all_data:
            print(f"Invalid operation! {piece_to_change} does not exist in the collection.")
            continue
        all_data[piece_to_change][1] = new_key
        print(f"Changed the key of {piece_to_change} to {new_key}!")
