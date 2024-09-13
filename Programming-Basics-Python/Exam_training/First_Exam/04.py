days = int(input())
total_rakia_litres = 0
total_degree_of_rakia = 0

for _ in range(1, days + 1):
    rakia_litres = float(input())
    degree_of_rakia = float(input())
    total_rakia_litres += rakia_litres
    total_degree_of_rakia += degree_of_rakia * rakia_litres

average_degree = total_degree_of_rakia / total_rakia_litres
print(f"Liter: {total_rakia_litres:.2f}")
print(f"Degrees: {average_degree:.2f}")


if average_degree > 42:
    print("Dilution with distilled water!")
elif average_degree >= 38:
    print("Super!")
elif average_degree < 38:
    print("Not good, you should baking!")
