number_of_names = int(input())
names_library = set()

for line in range(number_of_names):
    user_name = input()
    names_library.add(user_name)

for name in names_library:
    print(name)