movie_name = str(input())
days = int(input())
tickets = int(input())
price_ticket = float(input())
cinema_tax = float(input()) / 100

earning = (price_ticket * tickets) * days
cinema_tax_sum = earning * cinema_tax

print(f"The profit from the movie {movie_name} is {earning - cinema_tax_sum:.2f} lv.")
