best_points = 0
best_name = ""
points = 0
counter = 7

while True:
    movie_name = input()
    if movie_name == 'STOP':
        break

    for i in range(len(movie_name)):
        if 65 <= ord(movie_name[i]) <= 90:
            points += (ord(movie_name[i]) - len(movie_name))
        elif 97 <= ord(movie_name[i]) <= 122:
            points += (ord(movie_name[i]) - 2 * len(movie_name))
        else:
            points += (ord(movie_name[i]))

    if points > best_points:
        best_points = points
        best_name = movie_name

    points = 0
    counter -= 1
    if counter == 0:
        print("The limit is reached.")
        break

print(f'The best movie for you is {best_name} with {best_points} ASCII sum.')
