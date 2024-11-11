str1, str2 = input().split()
total_sum = 0

# Determine the minimum and maximum lengths
min_len = min(len(str1), len(str2))
max_len = max(len(str1), len(str2))

# Multiply corresponding characters for the length of the shorter string
for i in range(min_len):
    total_sum += ord(str1[i]) * ord(str2[i])

# Add the remaining characters from the longer string without multiplication
if len(str1) > len(str2):
    total_sum += sum(ord(char) for char in str1[min_len:])
else:
    total_sum += sum(ord(char) for char in str2[min_len:])

print(total_sum)
