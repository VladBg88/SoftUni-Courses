number = int(input())
collection = set()

for _ in range(number):
    user_input = input().split()
    for element in user_input:
        collection.add(element)

for element in collection:
    print(element)