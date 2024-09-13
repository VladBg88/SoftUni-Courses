import sys

RIGHT_BOUNDARY_P1 = 199
LEFT_BOUNDARY_P2 = 200
RIGHT_BOUNDARY_P2 = 399
LEFT_BOUNDARY_P3 = 400
RIGHT_BOUNDARY_P3 = 599
LEFT_BOUNDARY_P4 = 600
RIGHT_BOUNDARY_P4 = 799
LEFT_BOUNDARY_P5 = 800
RIGHT_BOUNDARY_P5 = sys.maxsize

num_count = int(input())
p1_count = 0
p2_count = 0
p3_count = 0
p4_count = 0
p5_count = 0

for _ in range(num_count):
    cur_number = int(input())

    if cur_number <= RIGHT_BOUNDARY_P1:
        p1_count += 1
    elif LEFT_BOUNDARY_P2 <= cur_number <= RIGHT_BOUNDARY_P2:
        p2_count += 1
    elif LEFT_BOUNDARY_P3 <= cur_number <= RIGHT_BOUNDARY_P3:
        p3_count += 1
    elif LEFT_BOUNDARY_P4 <= cur_number <= RIGHT_BOUNDARY_P4:
        p4_count += 1
    else:
        p5_count += 1

p1_count = (p1_count / num_count) * 100
p2_count = (p2_count / num_count) * 100
p3_count = (p3_count / num_count) * 100
p4_count = (p4_count / num_count) * 100
p5_count = (p5_count / num_count) * 100

print(f'{p1_count:.2f}%')
print(f'{p2_count:.2f}%')
print(f'{p3_count:.2f}%')
print(f'{p4_count:.2f}%')
print(f'{p5_count:.2f}%')
