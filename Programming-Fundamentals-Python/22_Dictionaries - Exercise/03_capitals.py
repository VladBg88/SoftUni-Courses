countries_names = input().split(', ')
cities_names = input().split(', ')
stack_dict = {country: city for country, city in zip(countries_names, cities_names)}

for country, city in stack_dict.items():
    print(f"{country} -> {city}")
