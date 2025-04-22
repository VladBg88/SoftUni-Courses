str1, str2 = input().split()
total_sum = 0
longer_string = 0

if len(str1) > len(str2):
    max_len = len(str1)
    min_len = len(str2)
    longer_string = 1
else:
    max_len = len(str2)
    min_len = len(str1)
    longer_string = 2

if longer_string == 1:

    for i in range(max_len):
        if i < min_len:
            total_sum += ord(str1[i]) * ord(str2[i])
        else:
            total_sum += ord(str1[i])

else:
    for i in range(max_len):
        if i < min_len:
            total_sum += ord(str1[i]) * ord(str2[i])
        else:
            total_sum += ord(str2[i])

print( total_sum)