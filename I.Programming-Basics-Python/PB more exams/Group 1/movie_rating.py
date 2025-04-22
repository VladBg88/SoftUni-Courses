movies_quantity_starting = int(input())
movie_name_highest_rating = ""
movie_rating_highest_rating = 0.0
movie_name_lowest_rating = ""
movie_rating_lowest_rating = 10.0
sum_rating = 0.0
movies_quantity = movies_quantity_starting

while movies_quantity_starting != 0:
    movie_name = str(input())
    movie_rating = float(input())
    sum_rating += movie_rating

    if movie_rating > movie_rating_highest_rating:
        movie_name_highest_rating = movie_name
        movie_rating_highest_rating = movie_rating

    if movie_rating < movie_rating_lowest_rating:
        movie_name_lowest_rating = movie_name
        movie_rating_lowest_rating = movie_rating

    movies_quantity_starting -= 1

print(f"{movie_name_highest_rating} is with highest rating: {movie_rating_highest_rating:.1f}")
print(f"{movie_name_lowest_rating} is with lowest rating: {movie_rating_lowest_rating:.1f}")
print(f"Average rating: {sum_rating / movies_quantity:.1f}")
