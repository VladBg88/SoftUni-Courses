list_of_integer = list(map(int, input().split()))
n_remove = int(input())

for i in range(n_remove):
    list_sorted = sorted(list_of_integer)
    to_remove = list_sorted[0]

    list_of_integer.remove(to_remove)

print(", ".join(map(str, list_of_integer)))
