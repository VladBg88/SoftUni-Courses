age = float(input("What's is your age?:"))
gender = input("What is your gender(f/m)?:")
if gender == "f":
    if age >= 16:
        print("Ms.")
    else:
        print("Miss")

if gender == "m":
    if age >= 16:
        print("Mr.")
    else:
        print("Master")
