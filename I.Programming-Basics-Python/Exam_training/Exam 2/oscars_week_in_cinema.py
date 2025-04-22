A_STAR_IS_BORN_NM = 7.50
A_STAR_IS_BORN_LX = 10.50
A_STAR_IS_BORN_ULX = 13.50
BOHEMIAN_RHAPSODY_NM = 7.35
BOHEMIAN_RHAPSODY_LX = 9.45
BOHEMIAN_RHAPSODY_ULX = 12.75
GREEN_BOOK_NM = 8.15
GREEN_BOOK_LX = 10.25
GREEN_BOOK_ULX = 13.25
THE_FAVOURITE_NM = 8.75
THE_FAVOURITE_LX = 11.55
THE_FAVOURITE_ULX = 13.95
total_price = 0

movie_name = str(input())
stage_type = str(input())
tickets_number = int(input())

if movie_name.lower() == "a star is born":
    if stage_type == "normal":
        total_price = A_STAR_IS_BORN_NM * tickets_number
    elif stage_type == "luxury":
        total_price = A_STAR_IS_BORN_LX * tickets_number
    elif stage_type == "ultra luxury":
        total_price = A_STAR_IS_BORN_ULX * tickets_number
elif movie_name.lower() == "bohemian rhapsody":
    if stage_type == "normal":
        total_price = BOHEMIAN_RHAPSODY_NM * tickets_number
    elif stage_type == "luxury":
        total_price = BOHEMIAN_RHAPSODY_LX * tickets_number
    elif stage_type == "ultra luxury":
        total_price = BOHEMIAN_RHAPSODY_ULX * tickets_number
elif movie_name.lower() == "green book":
    if stage_type == "normal":
        total_price = GREEN_BOOK_NM * tickets_number
    elif stage_type == "luxury":
        total_price = GREEN_BOOK_LX * tickets_number
    elif stage_type == "ultra luxury":
        total_price = GREEN_BOOK_ULX * tickets_number
elif movie_name.lower() == "the favourite":
    if stage_type == "normal":
        total_price = THE_FAVOURITE_NM * tickets_number
    elif stage_type == "luxury":
        total_price = THE_FAVOURITE_LX * tickets_number
    elif stage_type == "ultra luxury":
        total_price = THE_FAVOURITE_ULX * tickets_number

print(f"{movie_name} -> {total_price:.2f} lv.")
