desired_height = int(input())
starting_height = desired_height - 30
jumps_count = 0
limit_fails = 3

while True:
    jump = int(input())
    jumps_count += 1

    if jump > starting_height:
        limit_fails = 3
        if starting_height >= desired_height:
            print(f"Tihomir succeeded, he jumped over {starting_height}cm after {jumps_count} jumps.")
            break
        else:
            starting_height += 5
    elif jump <= starting_height:
        limit_fails -= 1
        if limit_fails == 0:
            print(f"Tihomir failed at {starting_height}cm after {jumps_count} jumps.")
            break
