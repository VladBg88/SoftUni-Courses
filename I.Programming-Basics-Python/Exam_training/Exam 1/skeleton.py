minutes = int(input())
seconds = int(input())
length_of_trace = float(input())
time_of_marin = int(input())

time_slow_down = length_of_trace / 120 * 2.5
control_time = minutes * 60 + seconds
time_of_marin = length_of_trace / 100 * time_of_marin - time_slow_down

if time_of_marin <= control_time:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {time_of_marin:.3f}.")
else:
    print(f"No, Marin failed! He was {time_of_marin - control_time:.3f} second slower.")
