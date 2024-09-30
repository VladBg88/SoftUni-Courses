zeros_to_back = input().split(', ')
zero_count = 0
result = []

for i in range(len(zeros_to_back)):
    if zeros_to_back[i] == '0':
        zero_count += 1
    else:
        result.append(int(zeros_to_back[i]))

result.extend([0] * zero_count)
print(result)
