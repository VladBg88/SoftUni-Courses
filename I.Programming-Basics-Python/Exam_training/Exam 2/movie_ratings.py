import sys

number_of_movies = int(input())
count_best_rating = -sys.maxsize
count_worst_rating = sys.maxsize
count_best_movie = ""
count_worst_movie = ""
count_average = 0.0

for _ in range(number_of_movies):
    name_of_movie = str(input())
    rating_of_movie = float(input())

    if rating_of_movie > count_best_rating:
        count_best_rating = rating_of_movie
        count_best_movie = name_of_movie
    elif rating_of_movie < count_worst_rating:
        count_worst_rating = rating_of_movie
        count_worst_movie = name_of_movie

    count_average += rating_of_movie

print(f"{count_best_movie} is with highest rating: {count_best_rating:.1f}")
print(f"{count_worst_movie} is with lowest rating: {count_worst_rating}")
print(f"Average rating: {count_average / number_of_movies:.1f}")
