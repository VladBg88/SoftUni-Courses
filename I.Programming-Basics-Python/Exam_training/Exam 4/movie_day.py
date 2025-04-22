time_for_pictures = int(input())
number_scenes = int(input())
time_of_scene = int(input())

preparation_time = time_for_pictures * 0.15
needed_time = preparation_time + time_of_scene * number_scenes

if time_for_pictures >= needed_time:
    print(f'You managed to finish the movie on time! You have {round(time_for_pictures - needed_time)} minutes left!')
elif time_for_pictures < needed_time:
    print(f'Time is up! To complete the movie you need {round(needed_time - time_for_pictures)} minutes.')
