n_number = int(input())
longest_intersection = []

for _ in range(n_number):
    first_numbers, second_numbers = input().split("-")
    first_start, first_end = [int(x) for x in first_numbers.split(",")]
    second_start, second_end = [int(x) for x in second_numbers.split(",")]
    first_set = set(x for x in range(first_start, first_end + 1))
    second_set = set(x for x in range(second_start, second_end + 1))
    intersection = first_set & second_set

    if len(intersection) > len(longest_intersection):
        longest_intersection = [x for x in intersection]

print(f"Longest intersection is {longest_intersection} with length {len(longest_intersection)}")
