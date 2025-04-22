movie_name = str(input())
days = int(input())
tickets_number = int(input())
price_of_ticket = float(input())
percent_cinema_tax = int(input()) / 100

all_tickets_sum = price_of_ticket * tickets_number * days
all_tickets_sum *= (1 - percent_cinema_tax)

print(f"The profit from the movie {movie_name} is {all_tickets_sum:.2f} lv.")

#test