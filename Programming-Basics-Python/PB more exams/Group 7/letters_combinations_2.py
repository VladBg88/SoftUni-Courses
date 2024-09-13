def generate_combinations(start, end, exclude):
    from itertools import product

    # Create a list of valid characters within the interval
    valid_chars = [chr(i) for i in range(ord(start), ord(end) + 1)]

    # Generate all possible 3-letter combinations
    all_combinations = [''.join(p) for p in product(valid_chars, repeat=3)]

    # Filter out combinations that contain the excluded character
    filtered_combinations = [comb for comb in all_combinations if exclude not in comb]

    # Print the valid combinations and their count
    print(" ".join(filtered_combinations), len(filtered_combinations))


# Example usage
start = input().strip()  # e.g., 'a'
end = input().strip()  # e.g., 'c'
exclude = input().strip()  # e.g., 'b'

generate_combinations(start, end, exclude)
