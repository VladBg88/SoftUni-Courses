favorite_book = str(input())
books_counter = 0

while True:
    searched_book = str(input())
    if searched_book == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {books_counter} books.")
        break

    if searched_book == favorite_book:
        print(f"You checked {books_counter} books and found it.")
        break

    books_counter += 1
